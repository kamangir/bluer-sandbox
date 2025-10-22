from bluer_objects.README.items import ImageItems

from bluer_sandbox.README.consts import bps_assets2

docs = (
    [
        {
            "path": "../docs/bps",
            "items": ImageItems(
                {f"{bps_assets2}/{index+1:02}.png": "" for index in range(3)}
            ),
        }
    ]
    + [
        {
            "path": f"../docs/bps/{doc}.md",
        }
        for doc in [
            "literature",
            "beacon-receiver",
            "beacon-and-receiver",
            "test-introspect",
        ]
    ]
    + [
        {
            "path": f"../../sandbox/bps/{doc}",
        }
        for doc in [
            "",
            "v1/",
        ]
    ]
)
