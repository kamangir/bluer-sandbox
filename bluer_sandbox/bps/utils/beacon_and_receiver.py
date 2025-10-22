#!/usr/bin/env python3
"""
Hybrid BLE Beacon + Receiver
----------------------------
Each node alternates between:
  • Advertising (x, y, σ) via BLE manufacturer data (0xFFFF)
  • Scanning for nearby nodes' beacons

Requires:
  - BlueZ >= 5.55 started with `--experimental`
  - D-Bus access to org.bluez (system bus)
"""

import asyncio
import struct
import time
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, dbus_property, method
from dbus_next import Variant, BusType, constants

from bluer_options.env import abcli_hostname


AD_IFACE = "org.bluez.LEAdvertisement1"
AD_PATH = "/org/bluez/example/advertisement0"
MFG_ID = 0xFFFF


# -------------------------------------------------------------------
# Advertisement object (registered via LEAdvertisingManager1)
# -------------------------------------------------------------------
class Advertisement(ServiceInterface):
    def __init__(self, node_id, payload):
        super().__init__(AD_IFACE)
        self.node_id = node_id
        self.payload = payload
        self._service_uuids = []

    @dbus_property()
    def Type(self) -> "s":
        return "peripheral"

    @Type.setter
    def Type(self, _value: "s"):
        pass

    @dbus_property()
    def LocalName(self) -> "s":
        return self.node_id

    @LocalName.setter
    def LocalName(self, _value: "s"):
        pass

    @dbus_property()
    def ManufacturerData(self) -> "a{qv}":
        return {MFG_ID: Variant("ay", self.payload)}

    @ManufacturerData.setter
    def ManufacturerData(self, _value: "a{qv}"):
        pass

    @dbus_property()
    def IncludeTxPower(self) -> "b":
        return True

    @IncludeTxPower.setter
    def IncludeTxPower(self, _value: "b"):
        pass

    @dbus_property()
    def ServiceUUIDs(self) -> "as":
        return self._service_uuids

    @ServiceUUIDs.setter
    def ServiceUUIDs(self, _value: "as"):
        pass

    @method()
    def Release(self):
        print(f"[{self.node_id}] advertisement released")


# -------------------------------------------------------------------
# Receiver helper
# -------------------------------------------------------------------
def parse_mdata(mdata_variant):
    """Decode manufacturer data Variant if Company ID 0xFFFF is present."""
    try:
        payload = mdata_variant[MFG_ID].value
        if len(payload) >= 12:
            return struct.unpack("<fff", bytes(payload[:12]))
    except Exception:
        pass
    return None


async def scan_once(bus, t_scan=3.0):
    """Listen for PropertiesChanged signals with ManufacturerData."""
    results = {}

    def handler(msg):
        if msg.message_type != constants.MessageType.SIGNAL:
            return
        if msg.interface != "org.freedesktop.DBus.Properties":
            return
        try:
            iface, changed, _ = msg.body
            if iface != "org.bluez.Device1":
                return
            if "ManufacturerData" not in changed:
                return
            mdata = changed["ManufacturerData"]
            parsed = parse_mdata(mdata)
            if parsed:
                x, y, sigma = parsed
                rssi = changed.get("RSSI", 0)
                addr = msg.path.split("/")[-1].replace("_", ":")
                results[addr] = (x, y, sigma, rssi)
                print(
                    f"[peer] {addr} RSSI={rssi:>4} pos=({x:.2f},{y:.2f}) σ={sigma:.2f}"
                )
        except Exception as e:
            print(f"[hybrid] handler error: {e}")

    bus.add_message_handler(handler)

    # Access adapter
    introspect = await bus.introspect("org.bluez", "/org/bluez/hci0")
    adapter_obj = bus.get_proxy_object("org.bluez", "/org/bluez/hci0", introspect)
    adapter_iface = adapter_obj.get_interface("org.bluez.Adapter1")

    # Enable active scanning
    try:
        await adapter_iface.call_set_discovery_filter(
            {
                "DuplicateData": Variant("b", True),
                "Transport": Variant("s", "le"),
            }
        )
    except Exception as e:
        print(f"[hybrid] warning: could not set discovery filter: {e}")

    # 🧩 Prime the device cache — ensures PropertiesChanged signals are delivered
    try:
        obj_mgr = bus.get_proxy_object(
            "org.bluez", "/", await bus.introspect("org.bluez", "/")
        )
        mgr_iface = obj_mgr.get_interface("org.freedesktop.DBus.ObjectManager")
        devices = await mgr_iface.call_get_managed_objects()
        print(f"[hybrid] cached {len(devices)} existing device entries")
    except Exception as e:
        print(f"[hybrid] could not get managed objects: {e}")

    # Begin scanning
    await adapter_iface.call_start_discovery()
    print("[hybrid] discovery started")

    await asyncio.sleep(t_scan)

    await adapter_iface.call_stop_discovery()
    print("[hybrid] discovery stopped")

    bus.remove_message_handler(handler)
    return results


# -------------------------------------------------------------------
# Main hybrid loop
# -------------------------------------------------------------------
async def main():
    node_id = abcli_hostname
    x, y, sigma = 1.0, 2.0, 0.5
    t_adv, t_scan = 2.0, 8.0  # seconds

    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    introspect = await bus.introspect("org.bluez", "/org/bluez/hci0")
    mgr = bus.get_proxy_object("org.bluez", "/org/bluez/hci0", introspect)
    leman = mgr.get_interface("org.bluez.LEAdvertisingManager1")

    print(f"[hybrid] node {node_id} ready (advertise {t_adv}s / scan {t_scan}s)")

    while True:
        # --- Advertise ---
        payload = struct.pack("<fff", x, y, sigma)
        adv = Advertisement(node_id, payload)
        bus.export(AD_PATH, adv)
        try:
            await leman.call_register_advertisement(AD_PATH, {})
            print(f"[hybrid] advertising {node_id} ...")
            await asyncio.sleep(t_adv)
        except Exception as e:
            print(f"[hybrid] advertise error: {e}")
        finally:
            try:
                await leman.call_unregister_advertisement(AD_PATH)
            except Exception:
                pass
            bus.unexport(AD_PATH)
            print("[hybrid] pause before scanning …")

        # --- Scan ---
        print("[hybrid] scanning ...")
        peers = await scan_once(bus, t_scan)
        if peers:
            for name, (px, py, ps, rssi) in peers.items():
                print(
                    f"[peer] {name:>10} RSSI={rssi:>4} pos=({px:.2f},{py:.2f}) σ={ps:.2f}"
                )
        else:
            print("[hybrid] no peers detected")

        await asyncio.sleep(0.5)


# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[hybrid] stopped")
