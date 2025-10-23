#!/usr/bin/env python3
# beacon_and_receiver.py — combined BLE advertiser + receiver (BlueZ + Bleak)
# Requires: dbus-next 0.2.x, bluetoothd --experimental, adapter powered on.

import asyncio
import struct
import signal
import dataclasses
import argparse
import time

from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, method, dbus_property
from dbus_next import Variant, BusType, Message, MessageType

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from blueness import module
from bluer_options.env import abcli_hostname
from bluer_options.terminal.functions import hr
from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

BUS_NAME = "org.bluez"
ADAPTER_PATH = "/org/bluez/hci0"
ADVERTISING_MGR_IFACE = "org.bluez.LEAdvertisingManager1"
AD_IFACE = "org.bluez.LEAdvertisement1"


# ----------------------------------------------------------------------
# Advertisement
class Advertisement(ServiceInterface):
    def __init__(self, name: str, x=0.0, y=0.0, sigma=1.0):
        super().__init__(AD_IFACE)
        self._name = name
        self._type = "peripheral"
        self._include_tx_power = True
        self._service_uuids = []
        self._mfg = {0xFFFF: struct.pack("<fff", x, y, sigma)}

    @dbus_property()
    def Type(self) -> "s":
        return self._type

    @Type.setter
    def Type(self, _value: "s"):
        pass

    @dbus_property()
    def LocalName(self) -> "s":
        return self._name

    @LocalName.setter
    def LocalName(self, _value: "s"):
        pass

    @dbus_property()
    def ServiceUUIDs(self) -> "as":
        return self._service_uuids

    @ServiceUUIDs.setter
    def ServiceUUIDs(self, _value: "as"):
        pass

    @dbus_property()
    def IncludeTxPower(self) -> "b":
        return self._include_tx_power

    @IncludeTxPower.setter
    def IncludeTxPower(self, _value: "b"):
        pass

    @dbus_property()
    def ManufacturerData(self) -> "a{qv}":
        return {0xFFFF: Variant("ay", self._mfg[0xFFFF])}

    @ManufacturerData.setter
    def ManufacturerData(self, _value: "a{qv}"):
        pass

    @method()
    def Release(self):
        logger.info(f"{NAME}: BlueZ requested Release() — advertisement unregistered.")


# ----------------------------------------------------------------------
# Advertiser helpers (Option A: unique D-Bus path each cycle)
async def register_advertisement(bus: MessageBus):
    # unique D-Bus object path per cycle
    ad_path = f"/org/bluez/example/advertisement{int(time.time() * 1000)}"

    adv = Advertisement(name=abcli_hostname, x=1.2, y=2.3, sigma=0.8)
    bus.export(ad_path, adv)
    await asyncio.sleep(0.5)

    msg = Message(
        destination=BUS_NAME,
        path=ADAPTER_PATH,
        interface=ADVERTISING_MGR_IFACE,
        member="RegisterAdvertisement",
        signature="oa{sv}",
        body=[ad_path, {}],
    )
    reply = await bus.call(msg)
    if reply.message_type == MessageType.ERROR:
        raise RuntimeError(f"RegisterAdvertisement failed: {reply.error_name}")

    return adv, ad_path


async def unregister_advertisement(bus: MessageBus, ad_path: str):
    try:
        msg = Message(
            destination=BUS_NAME,
            path=ADAPTER_PATH,
            interface=ADVERTISING_MGR_IFACE,
            member="UnregisterAdvertisement",
            signature="o",
            body=[ad_path],
        )
        await bus.call(msg)
    except Exception as e:
        logger.info(f"unregister_advertisement: {e}")

    try:
        bus.unexport(ad_path)
    except Exception:
        pass


# ----------------------------------------------------------------------
# Receiver
def to_dict(obj):
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    if hasattr(obj, "__dict__"):
        return vars(obj)
    if isinstance(obj, dict):
        return obj
    return {"repr": repr(obj)}


async def scan_for(timeout: float, grep: str = ""):
    def callback(device: BLEDevice, advertisement_data: AdvertisementData):
        if grep and (device.name is None or grep not in device.name):
            return
        logger.info(hr(width=30))
        logger.info(f"device name: {device.name}")
        logger.info(f"device address: {device.address}")
        try:
            logger.info(f"rssi: {advertisement_data.rssi}")
        except Exception:
            pass
        try:
            x_, y_, sigma_ = struct.unpack(
                "<fff", advertisement_data.manufacturer_data[0xFFFF]
            )
            logger.info(f"x: {x_:.2f}, y: {y_:.2f}, sigma: {sigma_:.2f}")
        except Exception:
            logger.info(advertisement_data)

    scanner = BleakScanner(detection_callback=callback)
    await scanner.start()
    logger.info(f"{NAME}: scanning for {timeout:.1f}s ...")
    await asyncio.sleep(timeout)
    await scanner.stop()
    logger.info(f"{NAME}: scan stopped.")


# ----------------------------------------------------------------------
# Combined loop
async def main(t_advertisement: float = 2.0, t_scan: float = 8.0, grep: str = ""):
    bus = MessageBus(bus_type=BusType.SYSTEM)
    await bus.connect()
    logger.info(f"{NAME}: connected to system bus as {bus.unique_name}")

    stop = asyncio.Event()

    def _sigint(*_):
        stop.set()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, _sigint)
        except NotImplementedError:
            pass

    while not stop.is_set():
        # --- advertise ---
        if t_advertisement > 0:
            try:
                adv, ad_path = await register_advertisement(bus)
                logger.info(
                    f"advertising {abcli_hostname} for {t_advertisement:.1f}s at {ad_path} ..."
                )
                await asyncio.sleep(t_advertisement)
                await unregister_advertisement(bus, ad_path)
                logger.info("advertisement stopped.")
            except Exception as e:
                logger.warning(f"advertise error: {e}")

        await asyncio.sleep(2)

        # --- scan ---
        if t_scan > 0:
            try:
                await scan_for(timeout=t_scan, grep=grep)
            except Exception as e:
                logger.info(f"scan error: {e}")

    logger.info(f"{NAME}: terminated.")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument("--grep", type=str, default="")
    parser.add_argument(
        "--t_advertisement", type=float, default=2.0, help="in seconds, -1: disable"
    )
    parser.add_argument(
        "--t_scan", type=float, default=8.0, help="in seconds, -1: disable"
    )
    args = parser.parse_args()

    asyncio.run(
        main(
            t_advertisement=args.t_advertisement,
            t_scan=args.t_scan,
            grep=args.grep,
        )
    )
