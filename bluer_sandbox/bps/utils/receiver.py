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


async def main(
    grep: str = "",
    timeout: float = 10.0,
):
    logger.info(f"{NAME}: LE Scan ...")

    def callback(
        device: BLEDevice,
        advertisement_data: AdvertisementData,
    ):
        if grep and (device.name is None or grep not in device.name):
            return

        logger.info(hr(width=30))

        logger.info(f"device name: {device.name}")
        logger.info(f"device address: {device.address}")

        if advertisement_data:
            logger.info(advertisement_data)

    await BleakScanner.discover(
        timeout=timeout,
        detection_callback=callback,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--grep",
        type=str,
        default="",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="in seconds",
    )
    args = parser.parse_args()

    asyncio.run(
        main(
            grep=args.grep,
            timeout=args.timeout,
        )
    )
