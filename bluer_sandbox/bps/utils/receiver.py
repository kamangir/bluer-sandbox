import asyncio
from bleak import BleakScanner, BleakAdvertisementData, BLEDevice
import argparse

from blueness import module
from bluer_options.terminal.functions import hr

from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


async def main(
    timeout: float = 10.0,
):
    logger.info(f"{NAME}: LE Scan ...")

    def cb(
        device: BLEDevice,
        advertisement_data: BleakAdvertisementData,
    ):
        logger("device info:")
        for key, value in vars(device).items():
            logger(f" - {key}: {value}")

        if advertisement_data:
            logger("advertisement data:")
            for key, value in vars(advertisement_data).items():
                logger.info(f" - {key}: {value}")

        hr(width=30)

    await BleakScanner.discover(timeout=10.0, detection_callback=cb)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="in seconds",
    )
    args = parser.parse_args()

    asyncio.run(
        main(
            timeout=args.timeout,
        )
    )
