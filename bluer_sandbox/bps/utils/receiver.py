import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
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

    def callback(
        device: BLEDevice,
        advertisement_data: AdvertisementData,
    ):
        logger.info("device info:")
        for key, value in vars(device).items():
            logger.info(f" - {key}: {value}")

        if advertisement_data:
            logger.info("advertisement data:")
            for key, value in vars(advertisement_data).items():
                logger.info(f" - {key}: {value}")

        hr(width=30)

    await BleakScanner.discover(
        timeout=timeout,
        detection_callback=callback,
    )


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
