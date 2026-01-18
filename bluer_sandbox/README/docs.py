import os

from bluer_objects.README.alias import list_of_aliases

from bluer_sandbox import NAME
from bluer_sandbox.README import aliases, arduino, bps, radar
from bluer_sandbox.README.items import items

docs = (
    [
        {
            "path": "../..",
            "cols": 3,
            "items": items,
            "macros": {
                "aliases:::": list_of_aliases(NAME),
            },
        },
        {
            "path": "../docs",
        },
        {
            "path": "../../sandbox",
        },
    ]
    + [
        {
            "path": f"../docs/{doc}.md",
        }
        for doc in [
            "arvancloud",
            "green",
            "offline_llm",
            "LSTM",
            "netcat",
            "tor",
            "v2ray",
        ]
    ]
    + aliases.docs
    + arduino.docs
    + bps.docs
    + radar.docs
)
