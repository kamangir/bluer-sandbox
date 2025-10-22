#!/usr/bin/env python3
"""
BLE Beacon + Receiver
---------------------
Broadcasts position data (x, y, σ) via BLE advertisements and
scans for other beacons broadcasting on manufacturer ID 0xFFFF.
"""

import asyncio
import struct
import threading
import time
from bluezero import adapter, advertisement
from bleak import BleakScanner
import argparse

from blueness import module
from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


# ---------------------------------------------------------------
# Beacon: broadcasts BLE advertisement packets
# ---------------------------------------------------------------
class Beacon:
    """Advertises (x, y, σ) via BLE manufacturer data."""

    def __init__(
        self,
        node_id: str | None = None,
        x: float = 0.0,
        y: float = 0.0,
        sigma: float = 1.0,
        interval_ms: int = 500,
    ):
        ble_adapter = adapter.Adapter()
        self.node_id = node_id or f"UGV-{ble_adapter.address[-5:].replace(':', '')}"
        self.x, self.y, self.sigma = x, y, sigma
        self.interval_ms = interval_ms
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._adv: advertisement.Advertisement | None = None

    # ---- Lifecycle ----------------------------------------------------------

    def start(self):
        """Start BLE advertising in a background thread."""
        if self._thread and self._thread.is_alive():
            logger.debug(f"[beacon] {self.node_id} already running")
            return
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        logger.info(f"[beacon] {self.node_id} advertising every {self.interval_ms} ms")

    def stop(self):
        """Stop advertising."""
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2.0)
            if self._thread.is_alive():
                logger.warning("[beacon] thread did not exit cleanly")
        logger.info(f"[beacon] {self.node_id} stopped")

    # ---- Internal -----------------------------------------------------------

    def _run(self):
        """Worker thread that runs BLE advertisement loop."""
        ble_adapter = adapter.Adapter()
        self._adv = advertisement.Advertisement(1, ble_adapter.address)
        self._adv.include_tx_power = True
        self._adv.appearance = 0
        self._adv.local_name = self.node_id
        self._adv.manufacturer_data = {
            0xFFFF: struct.pack("<fff", self.x, self.y, self.sigma)
        }

        try:
            self._adv.start()
            while not self._stop.is_set():
                time.sleep(self.interval_ms / 1000)
        except Exception as e:
            logger.warning(f"[beacon] exception in _run: {e}")
        finally:
            try:
                if self._adv:
                    logger.debug("[beacon] stopping advertisement …")
                    self._adv.stop()
            except Exception as e:
                logger.warning(f"[beacon] stop() failed: {e}")


# ---------------------------------------------------------------
# Receiver: scans BLE advertisements asynchronously (Bleak)
# ---------------------------------------------------------------
class Receiver:
    """Scans for BLE beacons broadcasting manufacturer data (0xFFFF)."""

    def __init__(self, scan_window_s: float = 2.0):
        self.scan_window_s = scan_window_s
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self.latest: dict[str, tuple[float, float, float, int, float]] = {}

    # ---- Lifecycle ----------------------------------------------------------

    def start(self):
        logger.info("[receiver] BLE scanner starting…")
        self._thread.start()

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2.0)
            if self._thread.is_alive():
                logger.warning("[receiver] thread did not exit cleanly")
        logger.info("[receiver] BLE scanner stopped")

    # ---- Internal -----------------------------------------------------------

    async def _scan_once(self):
        """Perform one BLE scan iteration and record visible beacons."""
        devices = await BleakScanner.discover(
            timeout=self.scan_window_s, return_adv=True
        )
        timestamp = time.time()

        iterable = (
            devices.items()
            if isinstance(devices, dict)
            else (
                devices
                if devices and isinstance(devices[0], tuple)
                else [(d, getattr(d, "advertisement_data", None)) for d in devices]
            )
        )

        for device, adv in iterable:
            name = getattr(adv, "local_name", None) or getattr(device, "name", None)
            if not name:
                continue

            md = getattr(adv, "manufacturer_data", None) or {}
            data = md.get(0xFFFF)
            if not data or len(data) < 12:
                continue

            x, y, sigma = struct.unpack("<fff", data[:12])
            self.latest[name] = (x, y, sigma, getattr(device, "rssi", 0), timestamp)
            logger.info(
                f"[receiver] {name} → RSSI={device.rssi:>4} dB  "
                f"pos=({x:.2f},{y:.2f}) σ={sigma:.2f}"
            )

    def _loop(self):
        """Main scanning loop."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while not self._stop.is_set():
            try:
                loop.run_until_complete(self._scan_once())
            except Exception as e:
                logger.warning(f"[receiver] scan loop error: {e}")
                time.sleep(1)


# ---------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--role",
        type=str,
        default="beacon",
        help="beacon | receiver | both",
    )
    args = parser.parse_args()

    do_beacon = args.role in ["beacon", "both"]
    do_receiver = args.role in ["receiver", "both"]

    beacon = Beacon() if do_beacon else None
    receiver = Receiver(scan_window_s=3.0) if do_receiver else None

    try:
        if do_beacon:
            beacon.start()

        if do_receiver:
            receiver.start()

        while True:
            time.sleep(5)
            if do_receiver:
                peers = list(receiver.latest)
                logger.info(f"[bps] known peers: {peers or '[]'}")

    except KeyboardInterrupt:
        logger.info("[bps] SIGINT received, shutting down …")
    finally:
        if do_beacon:
            beacon.stop()
        if do_receiver:
            receiver.stop()
        logger.info("[bps] exit complete ✅")
