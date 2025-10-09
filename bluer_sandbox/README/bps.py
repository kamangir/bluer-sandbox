from bluer_objects.README.items import ImageItems

from bluer_sandbox.README.consts import bps_assets2

docs = [
    {
        "path": f"../docs/bps.md",
        "items": ImageItems(
            {f"{bps_assets2}/{index:02}.png": "" for index in range(3)}
        ),
    },
]
