import os

from bluer_options.help.functions import get_help
from bluer_objects import file, README

from bluer_sandbox import NAME, VERSION, ICON, REPO_NAME
from bluer_sandbox.help.functions import help_functions
from bluer_sandbox.README import aliases, bps
from bluer_sandbox.README.items import items


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
            macros=readme.get("macros", {}),
        )
        for readme in [
            {
                "path": "../..",
                "cols": 2,
                "items": items,
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
                "offline_llm",
                "LSTM",
                "tor",
            ]
        ]
        + aliases.docs
        + bps.docs
    )
