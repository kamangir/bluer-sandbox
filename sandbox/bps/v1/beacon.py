#!/usr/bin/env python3
import asyncio
import struct
import time
from dbus_next.aio import MessageBus
from dbus_next import Message, MessageType, Variant
from dbus_next import BusType

BUS_NAME = "org.bluez"
ADAPTER_PATH = "/org/bluez/hci0"
AD_IFACE = "org.bluez.LEAdvertisingManager1"
AD_OBJ_PATH = "/org/bluez/example/advertisement0"
ADVERT_IFACE = "org.bluez.LEAdvertisement1"


class Advertisement:
    def __init__(self, name: str, x=0.0, y=0.0, sigma=1.0):
        self.name = name
        self.x, self.y, self.sigma = x, y, sigma
        self.service_uuids = []
        self.manufacturer_data = {0xFFFF: list(struct.pack("<fff", x, y, sigma))}
        self.type = "peripheral"
        self.include_tx_power = True

    def get_properties(self):
        return {
            ADVERT_IFACE: {
                "Type": Variant("s", self.type),
                "LocalName": Variant("s", self.name),
                "ServiceUUIDs": Variant("as", self.service_uuids),
                "ManufacturerData": Variant(
                    "a{qv}",
                    {0xFFFF: Variant("ay", bytes(self.manufacturer_data[0xFFFF]))},
                ),
                "IncludeTxPower": Variant("b", self.include_tx_power),
            }
        }

    def get_path(self):
        return AD_OBJ_PATH


async def main():
    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()

    # register advertisement object on D-Bus
    adv = Advertisement("TEST-PI")
    props = adv.get_properties()

    await bus.export(AD_OBJ_PATH, {ADVERT_IFACE: {"Release": lambda: None}})

    # register with BlueZ advertising manager
    msg = Message(
        destination=BUS_NAME,
        path=ADAPTER_PATH,
        interface=AD_IFACE,
        member="RegisterAdvertisement",
        signature="oa{sv}",
        body=[adv.get_path(), {}],
    )
    reply = await bus.call(msg)
    if reply.message_type == MessageType.ERROR:
        print(f"[!] Failed to register advertisement: {reply.error_name}")
        return

    print("[Beacon] Advertising started as TEST-PI … Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        msg = Message(
            destination=BUS_NAME,
            path=ADAPTER_PATH,
            interface=AD_IFACE,
            member="UnregisterAdvertisement",
            signature="o",
            body=[adv.get_path()],
        )
        await bus.call(msg)
        print("\n[Beacon] Advertisement stopped.")


if __name__ == "__main__":
    asyncio.run(main())
