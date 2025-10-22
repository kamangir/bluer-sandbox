import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
import argparse
import dataclasses

from blueness import module
from bluer_options.terminal.functions import hr
from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def to_dict(obj):
    """Safely convert a dataclass or object to a dict."""
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    elif hasattr(obj, "__dict__"):
        return vars(obj)
    elif isinstance(obj, dict):
        return obj
    else:
        return {"repr": repr(obj)}


async def main(timeout: float = 10.0):
    logger.info(f"{NAME}: LE Scan ...")

    def callback(device: BLEDevice, advertisement_data: AdvertisementData):
        logger.info("device info:")
        for key, value in to_dict(device).items():
            logger.info(f" - {key}: {value}")

        if advertisement_data:
            logger.info("advertisement data:")
            for key, value in to_dict(advertisement_data).items():
                logger.info(f" - {key}: {value}")

        logger.info(hr(width=30))

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

    asyncio.run(main(timeout=args.timeout))
