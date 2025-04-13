import os

from bluer_options.help.functions import get_help
from bluer_objects import file, README

from bluer_sandbox import NAME, VERSION, ICON, REPO_NAME
from bluer_sandbox.help.functions import help_functions


items = README.Items(
    [
        {
            "name": "`@notebooks`",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
            "description": "jupyter Notebooks",
            "url": "./bluer_sandbox/assets/template.ipynb",
        },
        {
            "name": "offline LLM",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
            "description": "using [llama.cpp](https://github.com/ggerganov/llama.cpp)",
            "url": "./bluer_sandbox/docs/offline_llm.md",
        },
    ]
)


def build():
    return all(
        README.build(
            items=readme.get("items", []),
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
        )
        for readme in [
            {
                "path": "..",
                "items": items,
            },
            {
                "path": "docs/offline_llm.md",
            },
        ]
    )
