#!/usr/bin/env python3
"""
Beacon-Exchange (time-division hybrid)
--------------------------------------
Each node alternates between:
  • advertising (x, y, σ) for a short burst
  • scanning for peers for a few seconds

All communication happens via BLE manufacturer data (0xFFFF).

Requirements:
  • BlueZ ≥ 5.55
  • bluetoothd started with --experimental
"""

import asyncio
import struct
import time
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, dbus_property, method
from dbus_next import Variant, BusType, constants, Message

from bluer_options.env import abcli_hostname  # your host alias utility


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

    # --- Required properties ---
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
# Receiver helper (passive scan using D-Bus signals + fallback poll)
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


def _parse_device1_from_interfaces_added(msg):
    """Return (name, rssi, mdata_variant) if msg is BlueZ Device1 InterfacesAdded."""
    try:
        iface_data = msg.body[1]
        props = iface_data.get("org.bluez.Device1")
        if not props:
            return None
        name = props.get("Name", "<unknown>")
        rssi = props.get("RSSI", 0)
        mdata = props.get("ManufacturerData")
        return (name, rssi, mdata)
    except Exception:
        return None


async def scan_once(bus, t_scan=3.0):
    """
    Listen for BlueZ's InterfacesAdded(Device1) during discovery and also
    poll GetManagedObjects at the end as a fallback.
    """
    match_rule = (
        "type='signal',sender='org.bluez',"
        "path_namespace='/org/bluez',"
        "interface='org.freedesktop.DBus.ObjectManager',"
        "member='InterfacesAdded'"
    )

    # Subscribe to BlueZ signals
    await bus.call(
        Message(
            destination="org.freedesktop.DBus",
            path="/org/freedesktop/DBus",
            interface="org.freedesktop.DBus",
            member="AddMatch",
            signature="s",
            body=[match_rule],
        )
    )

    results = {}

    def handler(msg):
        parsed = _parse_device1_from_interfaces_added(msg)
        if not parsed:
            return
        name, rssi, mdata = parsed
        if not mdata:
            return
        parsed_payload = parse_mdata(mdata)
        if parsed_payload:
            x, y, sigma = parsed_payload
            results[name] = (x, y, sigma, rssi)

    bus.add_message_handler(handler)
    try:
        await asyncio.sleep(t_scan)
    finally:
        bus.remove_message_handler(handler)

    # ---- Poll fallback: scrape GetManagedObjects for any dev_* we missed ----
    try:
        om_introspect = await bus.introspect("org.bluez", "/")
        root = bus.get_proxy_object("org.bluez", "/", om_introspect)
        om = root.get_interface("org.freedesktop.DBus.ObjectManager")
        objs = await om.call_get_managed_objects()
        for path, ifaces in objs.items():
            if not path.startswith("/org/bluez/hci0/dev_"):
                continue
            dev = ifaces.get("org.bluez.Device1")
            if not dev:
                continue
            mdata = dev.get("ManufacturerData")
            if not mdata:
                continue
            parsed_payload = parse_mdata(mdata)
            if not parsed_payload:
                continue
            name = dev.get("Name", "<unknown>")
            rssi = dev.get("RSSI", 0)
            x, y, sigma = parsed_payload
            results[name] = (x, y, sigma, rssi)
    except Exception:
        pass

    return results


# -------------------------------------------------------------------
# Main hybrid node: advertise, then scan, repeatedly
# -------------------------------------------------------------------
async def main():
    node_id = abcli_hostname
    x, y, sigma = 1.0, 2.0, 0.5
    t_adv, t_scan = 1.0, 4.0  # seconds

    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    # Get adapter + LE advertising manager
    introspect = await bus.introspect("org.bluez", "/org/bluez/hci0")
    mgr = bus.get_proxy_object("org.bluez", "/org/bluez/hci0", introspect)
    leman = mgr.get_interface("org.bluez.LEAdvertisingManager1")
    adapter_iface = mgr.get_interface("org.bluez.Adapter1")

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
            try:
                bus.unexport(AD_PATH)
            except Exception:
                pass

        await asyncio.sleep(0.3)

        # --- Scan ---
        print("[hybrid] scanning ...")
        try:
            await adapter_iface.call_start_discovery()
            print("[hybrid] discovery started")
            await asyncio.sleep(1.0)
        except Exception as e:
            print(f"[hybrid] start_discovery failed: {e}")

        peers = await scan_once(bus, t_scan)

        try:
            await adapter_iface.call_stop_discovery()
            print("[hybrid] discovery stopped")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"[hybrid] stop_discovery failed: {e}")

        if peers:
            for name, (px, py, ps, rssi) in peers.items():
                print(
                    f"[peer] {name:>12} RSSI={rssi:>4} dB  "
                    f"pos=({px:.2f},{py:.2f}) σ={ps:.2f}"
                )
        else:
            print("[hybrid] no peers detected")

        await asyncio.sleep(0.5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[hybrid] stopped")
