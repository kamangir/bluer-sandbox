#!/usr/bin/env python3
import asyncio
import struct
import time
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, method, dbus_property
from dbus_next import Variant, BusType, Message, MessageType

BUS_NAME = "org.bluez"
ADAPTER_PATH = "/org/bluez/hci0"
AD_IFACE = "org.bluez.LEAdvertisingManager1"
AD_OBJ_PATH = "/org/bluez/example/advertisement0"
ADVERT_IFACE = "org.bluez.LEAdvertisement1"


class Advertisement(ServiceInterface):
    def __init__(self, name: str, x=0.0, y=0.0, sigma=1.0):
        super().__init__(ADVERT_IFACE)
        self.name = name
        self.x, self.y, self.sigma = x, y, sigma
        self.service_uuids = []
        self.manufacturer_data = {0xFFFF: struct.pack("<fff", x, y, sigma)}
        self.type = "peripheral"
        self.include_tx_power = True

    # ---- read-only properties (with dummy setters for safety) ----
    @dbus_property()
    def Type(self) -> "s":
        return self.type

    @Type.setter
    def Type(self, value: "s"):
        pass

    @dbus_property()
    def LocalName(self) -> "s":
        return self.name

    @LocalName.setter
    def LocalName(self, value: "s"):
        pass

    @dbus_property()
    def ServiceUUIDs(self) -> "as":
        return self.service_uuids

    @ServiceUUIDs.setter
    def ServiceUUIDs(self, value: "as"):
        pass

    @dbus_property()
    def IncludeTxPower(self) -> "b":
        return self.include_tx_power

    @IncludeTxPower.setter
    def IncludeTxPower(self, value: "b"):
        pass

    @dbus_property()
    def ManufacturerData(self) -> "a{qv}":
        return {0xFFFF: Variant("ay", self.manufacturer_data[0xFFFF])}

    @ManufacturerData.setter
    def ManufacturerData(self, value: "a{qv}"):
        pass

    # ---- BlueZ will call this when unregistering ----
    @method()
    def Release(self):
        print("[Beacon] Advertisement released by BlueZ")


async def main():
    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    adv = Advertisement("TEST-PI", x=1.2, y=2.3, sigma=0.8)
    bus.export(AD_OBJ_PATH, adv)

    # Give D-Bus a moment to register the object before BlueZ introspects it
    await asyncio.sleep(1.0)

    msg = Message(
        destination=BUS_NAME,  # still talk *to* org.bluez
        path=ADAPTER_PATH,
        interface=AD_IFACE,
        member="RegisterAdvertisement",
        signature="oa{sv}",
        body=[AD_OBJ_PATH, {}],
    )
    reply = await bus.call(msg)
    if reply.message_type == MessageType.ERROR:
        print(f"[!] Failed to register advertisement: {reply.error_name}")
        return

    print("[Beacon] Advertising started as TEST-PI … Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
            print("advertising...")
    except KeyboardInterrupt:
        msg = Message(
            destination=BUS_NAME,
            path=ADAPTER_PATH,
            interface=AD_IFACE,
            member="UnregisterAdvertisement",
            signature="o",
            body=[AD_OBJ_PATH],
        )
        await bus.call(msg)
        print("\n[Beacon] Advertisement stopped.")


if __name__ == "__main__":
    asyncio.run(main())
