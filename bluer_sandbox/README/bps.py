from bluer_objects.README.items import ImageItems

from bluer_sandbox.README.consts import bps_assets2

docs = [
    {
        "path": "../docs/bps.md",
        "items": ImageItems(
            {f"{bps_assets2}/{index+1:02}.png": "" for index in range(3)}
        ),
    },
]
