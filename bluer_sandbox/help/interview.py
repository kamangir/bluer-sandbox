from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@sandbox",
            "interview",
            "<what>",
            "<args>",
        ],
        "interview/<what> <args>.",
        mono=mono,
    )


help_functions = {
    "": help,
}
