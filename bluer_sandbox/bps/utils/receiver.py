import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
import argparse
import dataclasses
import signal
import struct

from blueness import module
from bluer_options.terminal.functions import hr
from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def to_dict(obj):
    """Safely convert a dataclass or object to a dict."""
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)

    if hasattr(obj, "__dict__"):
        return vars(obj)

    if isinstance(obj, dict):
        return obj

    return {"repr": repr(obj)}


async def main(
    grep: str = "",
    timeout: float = 10.0,
):
    logger.info(f"{NAME}: LE Scan for {timeout:.1f}s (Ctrl+C to stop) ...")

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
            log_advertisement_data = True

            if 0xFFFF in advertisement_data:
                try:
                    x_, y_, sigma_ = struct.unpack("<fff", advertisement_data[0xFFFF])
                    logger.info(f"x: {x_:.2f}, y: {y_:.2f}, sigma: {sigma_:.2f}")
                    log_advertisement_data = False
                except Exception as e:
                    logger.warning(f"cannot unpack payload: {e}")

            if log_advertisement_data:
                logger.info(advertisement_data)

    scanner = BleakScanner(detection_callback=callback)
    await scanner.start()
    logger.info("scanning started...")

    stop_event = asyncio.Event()

    def handle_sigint():
        logger.info("Ctrl+C detected, stopping scan ...")
        stop_event.set()

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, handle_sigint)

    try:
        # wait either for timeout or Ctrl+C
        await asyncio.wait_for(stop_event.wait(), timeout=timeout)
    except asyncio.TimeoutError:
        logger.info(f"timeout reached after {timeout:.1f}s.")

    await scanner.stop()
    logger.info("scan stopped.")


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

    asyncio.run(main(grep=args.grep, timeout=args.timeout))
