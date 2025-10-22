#!/usr/bin/env python3
"""
Beacon-Exchange (time-division)
Each node alternates between:
  • advertising (x, y, σ) for ~1 s
  • scanning for peers for ~T_scan s
All communication happens via BLE manufacturer data (0xFFFF).
"""

import asyncio, struct, time
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, dbus_property, method
from dbus_next import Variant, BusType, constants

from bluer_options.env import abcli_hostname

AD_IFACE = "org.bluez.LEAdvertisement1"
AD_PATH = "/org/bluez/example/advertisement0"
MFG_ID = 0xFFFF


# ----- Advertisement object ---------------------------------------------------
class Advertisement(ServiceInterface):
    def __init__(self, node_id, payload):
        super().__init__(AD_IFACE)
        self.node_id = node_id
        self.payload = payload

    @dbus_property()
    def Type(self) -> "s":
        return "peripheral"

    @dbus_property()
    def LocalName(self) -> "s":
        return self.node_id

    @dbus_property()
    def ManufacturerData(self) -> "a{qv}":
        return {MFG_ID: Variant("ay", self.payload)}

    @dbus_property()
    def IncludeTxPower(self) -> "b":
        return True

    @method()
    def Release(self):
        pass


# ----- Receiver handler -------------------------------------------------------
def parse_mdata(mdata_variant):
    try:
        payload = mdata_variant[MFG_ID].value
        if len(payload) >= 12:
            return struct.unpack("<fff", bytes(payload[:12]))
    except Exception:
        return None


async def scan_once(bus, t_scan=3.0):
    """Listen for advertisement signals for t_scan seconds."""
    match = "type='signal',interface='org.freedesktop.DBus.ObjectManager',member='InterfacesAdded'"
    await bus.call_add_match(match)
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
            mdata = props["ManufacturerData"]
            parsed = parse_mdata(mdata)
            if parsed:
                x, y, sigma = parsed
                results[name] = (x, y, sigma, rssi)
        except Exception:
            pass

    bus.add_message_handler(handler)
    await asyncio.sleep(t_scan)
    bus.remove_message_handler(handler)
    return results


# ----- Main loop --------------------------------------------------------------
async def main():
    node_id = abcli_hostname
    x, y, sigma = 1.0, 2.0, 0.5
    t_adv, t_scan = 1.0, 4.0  # seconds

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
            print(f"[hybrid] advertising {node_id} …")
            await asyncio.sleep(t_adv)
        except Exception as e:
            print(f"[hybrid] advertise error: {e}")
        finally:
            try:
                await leman.call_unregister_advertisement(AD_PATH)
            except Exception:
                pass

        # --- Scan ---
        print("[hybrid] scanning …")
        peers = await scan_once(bus, t_scan)
        if peers:
            for name, (px, py, ps, rssi) in peers.items():
                print(
                    f"[peer] {name:>10} RSSI={rssi:>4} pos=({px:.2f},{py:.2f}) σ={ps:.2f}"
                )
        else:
            print("[hybrid] no peers detected")
        await asyncio.sleep(0.2)  # small idle gap


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[hybrid] stopped")
