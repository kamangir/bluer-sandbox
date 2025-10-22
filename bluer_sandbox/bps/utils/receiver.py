import asyncio
from bleak import BleakScanner


async def main():
    print("LE Scan ...")

    def cb(d, ad):
        name = d.name or ""
        print(f"{d.address} {name}".strip())

    await BleakScanner.discover(timeout=None, detection_callback=cb)


asyncio.run(main())
