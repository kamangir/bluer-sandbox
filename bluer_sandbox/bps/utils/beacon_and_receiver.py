#!/usr/bin/env python3
"""
Hybrid BLE Beacon & Receiver (time-division)
--------------------------------------------
Each node alternates between:
  • Advertising its (x, y, σ) via BLE manufacturer data (0xFFFF)
  • Scanning for other beacons’ advertisements

Optimized for Raspberry Pi controllers that need a pause between
advertise ↔ scan transitions (BlueZ 5.55+ with --experimental).
"""

import asyncio
import struct
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, dbus_property, method
from dbus_next import Variant, BusType, Message, constants

from bluer_options.env import abcli_hostname

AD_IFACE = "org.bluez.LEAdvertisement1"
AD_PATH = "/org/bluez/example/advertisement0"
MFG_ID = 0xFFFF


# -------------------------------------------------------------------
# Advertisement object
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
# Receiver helper (passive scan using D-Bus signals)
# -------------------------------------------------------------------
def parse_mdata(mdata_variant):
    try:
        payload = mdata_variant[MFG_ID].value
        if len(payload) >= 12:
            return struct.unpack("<fff", bytes(payload[:12]))
    except Exception:
        pass
    return None


async def scan_once(bus: MessageBus, t_scan: float = 3.0):
    """Listen for advertisement signals for t_scan seconds."""
    # subscribe to InterfacesAdded events
    add_match_msg = Message(
        destination="org.freedesktop.DBus",
        path="/org/freedesktop/DBus",
        interface="org.freedesktop.DBus",
        member="AddMatch",
        signature="s",
        body=[
            "type='signal',interface='org.freedesktop.DBus.ObjectManager',member='InterfacesAdded'"
        ],
    )
    await bus.call(add_match_msg)

    results = {}

    def handler(msg):
        if msg.message_type != constants.MessageType.SIGNAL:
            return
        try:
            iface_data = msg.body[1]
            props = iface_data.get("org.bluez.Device1")
            if not props or "ManufacturerData" not in props:
                return
            name = props.get("Name", "<unknown>")
            rssi = props.get("RSSI", 0)
            parsed = parse_mdata(props["ManufacturerData"])
            if parsed:
                x, y, sigma = parsed
                results[name] = (x, y, sigma, rssi)
        except Exception:
            pass

    bus.add_message_handler(handler)
    await asyncio.sleep(t_scan)
    bus.remove_message_handler(handler)
    return results


# -------------------------------------------------------------------
# Main hybrid node
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

        print("[hybrid] pause before scanning …")
        await asyncio.sleep(2.0)

        # --- Scan ---
        print("[hybrid] scanning ...")
        peers = await scan_once(bus, t_scan)
        if peers:
            for name, (px, py, ps, rssi) in peers.items():
                print(
                    f"[peer] {name:>10}  RSSI={rssi:>4} dB  "
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
