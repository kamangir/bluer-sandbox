#!/usr/bin/env python3
"""
Hybrid BLE Beacon + Receiver (D-Bus advertise + Bleak scan)
-----------------------------------------------------------
Each node alternates between:
  • Advertising (x, y, σ) via BLE manufacturer data (0xFFFF)
  • Scanning for nearby nodes’ beacons using Bleak

Tested on Raspberry Pi OS / BlueZ 5.75 / Bleak ≥ 0.22.
"""

import asyncio
import struct
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, dbus_property, method
from dbus_next import Variant, BusType
from bleak import BleakScanner
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
    def Type(self, _):
        pass

    @dbus_property()
    def LocalName(self) -> "s":
        return self.node_id

    @LocalName.setter
    def LocalName(self, _):
        pass

    @dbus_property()
    def ManufacturerData(self) -> "a{qv}":
        return {MFG_ID: Variant("ay", self.payload)}

    @ManufacturerData.setter
    def ManufacturerData(self, _):
        pass

    @dbus_property()
    def IncludeTxPower(self) -> "b":
        return True

    @IncludeTxPower.setter
    def IncludeTxPower(self, _):
        pass

    @dbus_property()
    def ServiceUUIDs(self) -> "as":
        return self._service_uuids

    @ServiceUUIDs.setter
    def ServiceUUIDs(self, _):
        pass

    @method()
    def Release(self):
        print(f"[{self.node_id}] advertisement released")


# -------------------------------------------------------------------
# Bleak scanner helper
# -------------------------------------------------------------------
async def scan_once_bleak(t_scan=5.0):
    """Perform a BLE scan using Bleak and parse manufacturer data."""
    results = {}
    print(f"[hybrid] bleak scanning for {t_scan:.1f}s …")

    try:
        devices = await BleakScanner.discover(timeout=t_scan)
    except Exception as e:
        print(f"[hybrid] scan error: {e}")
        return results

    for d in devices:
        # Compatible with Bleak ≥0.22 (advertisement_data) and older versions (metadata)
        adv = getattr(d, "advertisement_data", None)
        mdata = getattr(adv, "manufacturer_data", None)

        if mdata is None:
            # fallback for older Bleak
            mdata = getattr(d, "metadata", {}).get("manufacturer_data", {})

        if not isinstance(mdata, dict) or MFG_ID not in mdata:
            continue

        data = mdata[MFG_ID]
        if len(data) < 12:
            continue

        x, y, sigma = struct.unpack("<fff", bytes(data[:12]))
        results[d.address] = (x, y, sigma, d.rssi)
        print(
            f"[peer] {d.address} RSSI={d.rssi:>4} pos=({x:.2f},{y:.2f}) σ={sigma:.2f}"
        )

    if not results:
        print("[hybrid] no peers detected")
    return results


# -------------------------------------------------------------------
# Main hybrid loop
# -------------------------------------------------------------------
async def main():
    node_id = abcli_hostname
    x, y, sigma = 1.0, 2.0, 0.5
    t_adv, t_scan = 2.0, 8.0

    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    introspect = await bus.introspect("org.bluez", "/org/bluez/hci0")
    mgr = bus.get_proxy_object("org.bluez", "/org/bluez/hci0", introspect)
    leman = mgr.get_interface("org.bluez.LEAdvertisingManager1")

    print(f"[hybrid] node {node_id} ready (advertise {t_adv}s / scan {t_scan}s)")

    while True:
        # --- Advertise phase ---
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
            bus.unexport(AD_PATH)
            print("[hybrid] pause before scanning …")

        # --- Scan phase ---
        await scan_once_bleak(t_scan)

        # --- Adapter cooldown ---
        await asyncio.sleep(1.0)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[hybrid] stopped")
