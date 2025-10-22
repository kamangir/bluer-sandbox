import asyncio
import struct
import threading
import time
from bluezero import adapter, advertisement
from bleak import BleakScanner


# ---------------------------------------------------------------
# Beacon: broadcasts BLE advertisement packets (pure Python)
# ---------------------------------------------------------------
class Beacon:
    # pylint: disable=too-many-positional-arguments
    def __init__(
        self,
        node_id: str,
        x: float = 0.0,
        y: float = 0.0,
        sigma: float = 1.0,
        interval_ms: int = 500,
    ):
        """
        node_id: short identifier (e.g., 'AZ-0111')
        x, y: current position estimate (m)
        sigma: position uncertainty (m)
        interval_ms: advertising interval in milliseconds
        """
        self.node_id = node_id
        self.x, self.y, self.sigma = x, y, sigma
        self.interval_ms = interval_ms
        self._adv = None
        self._thread = None
        self._stop = threading.Event()

    def start(self):
        """Start BLE advertising in a background thread."""
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        print(
            f"[Beacon] {self.node_id} started advertising every {self.interval_ms} ms"
        )

    def stop(self):
        """Stop advertising."""
        self._stop.set()
        if self._adv:
            self._adv.stop()
        if self._thread:
            self._thread.join()
        print(f"[Beacon] {self.node_id} stopped")

    def _run(self):
        ble_adapter = adapter.Adapter()
        self._adv = advertisement.Advertisement(1, ble_adapter.address)
        self._adv.include_tx_power = True
        self._adv.appearance = 0
        self._adv.local_name = self.node_id

        # Pack simple manufacturer payload: x, y, sigma
        payload = struct.pack("<fff", self.x, self.y, self.sigma)
        self._adv.manufacturer_data = {0xFFFF: payload}

        self._adv.start()

        # Loop keeps advertisement alive until stop() called
        while not self._stop.is_set():
            time.sleep(self.interval_ms / 1000.0)
        self._adv.stop()


# ---------------------------------------------------------------
# Receiver: scans BLE advertisements asynchronously (Bleak)
# ---------------------------------------------------------------
class Receiver:
    def __init__(self, scan_window_s: float = 2.0):
        """
        scan_window_s: duration of each scan iteration
        """
        self.scan_window_s = scan_window_s
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._stop = threading.Event()
        self.latest = {}  # {node_id: (x, y, sigma, rssi, timestamp)}

    def start(self):
        print("[Receiver] BLE scanner starting…")
        self._thread.start()

    def stop(self):
        self._stop.set()
        self._thread.join()
        print("[Receiver] BLE scanner stopped")

    async def _scan_once(self):
        # Bleak 1.1.x returns a list of (device, adv_data) tuples
        devices = await BleakScanner.discover(
            timeout=self.scan_window_s,
            return_adv=True,
        )
        t = time.time()

        for device, adv_data in devices:
            name = adv_data.local_name or device.name
            if not name:
                continue

            md = adv_data.manufacturer_data or {}

            if 0xFFFF in md and len(md[0xFFFF]) >= 12:
                x, y, sigma = struct.unpack("<fff", md[0xFFFF][:12])
                self.latest[name] = (x, y, sigma, device.rssi, t)
                print(
                    f"[Receiver] {name} → RSSI={device.rssi}  pos=({x:.2f},{y:.2f}) σ={sigma:.2f}"
                )

    def _loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while not self._stop.is_set():
            loop.run_until_complete(self._scan_once())


# ---------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------
if __name__ == "__main__":
    beacon = Beacon("AZ-0111", x=1.2, y=2.3, sigma=0.8)
    receiver = Receiver(scan_window_s=3.0)

    try:
        beacon.start()
        receiver.start()
        while True:
            time.sleep(5)
            print(f"Known peers: {list(receiver.latest.keys())}")
    except KeyboardInterrupt:
        print("Shutting down…")
    finally:
        beacon.stop()
        receiver.stop()
