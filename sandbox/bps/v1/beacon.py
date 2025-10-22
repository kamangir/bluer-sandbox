import asyncio, struct
from bleak.advertisement import BleakAdvertiser


async def main():
    payload = struct.pack("<fff", 1.0, 2.0, 3.0)
    adv = BleakAdvertiser(local_name="TEST-PI")
    adv.manufacturer_data = {0xFFFF: payload}
    async with adv:
        print("Advertising... (Ctrl+C to stop)")
        while True:
            await asyncio.sleep(1)


asyncio.run(main())
