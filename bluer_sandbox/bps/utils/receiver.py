import asyncio
import argparse
import dataclasses
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from blueness import module
from bluer_options.terminal.functions import hr
from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def to_dict(obj):
    """Convert BLE-related objects to dict safely for logging."""
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    if hasattr(obj, "__dict__"):
        return vars(obj)
    if isinstance(obj, dict):
        return obj
    return {"value": repr(obj)}


def log_object(title: str, obj):
    """Pretty-print the contents of a BLE object."""
    logger.info(f"{title}:")
    data = to_dict(obj)
    if not data:
        logger.info("  (empty)")
        return
    for key, value in data.items():
        logger.info(f"  - {key}: {value}")


async def main(timeout: float = 10.0):
    logger.info(f"{NAME}: starting BLE scan for {timeout:.1f}s ...")

    def callback(device: BLEDevice, advertisement_data: AdvertisementData):
        log_object("🔹 Device", device)
        log_object("🔸 Advertisement", advertisement_data)
        hr(width=40)

    await BleakScanner.discover(timeout=timeout, detection_callback=callback)
    logger.info(f"{NAME}: scan complete ✅")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="scan duration in seconds",
    )
    args = parser.parse_args()

    try:
        asyncio.run(main(timeout=args.timeout))
    except KeyboardInterrupt:
        logger.warning(f"{NAME}: interrupted by user.")
    except Exception as e:
        logger.exception(f"{NAME}: error during BLE scan: {e}")
