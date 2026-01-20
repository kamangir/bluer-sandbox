from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_cd(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@sos",
            "cd",
        ],
        "cd sos folder.",
        mono=mono,
    )


def help_env(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@sos",
            "env",
            f"[{options}]",
        ],
        "sos += env.",
        mono=mono,
    )


def help_git(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,repo=<repo-name>", mono=mono)

    return show_usage(
        [
            "@sos",
            "git",
            f"[{options}]",
        ],
        "sos += git.",
        mono=mono,
    )


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@sos",
            "open",
        ],
        "open sos folder.",
        mono=mono,
    )


help_functions = {
    "cd": help_cd,
    "env": help_env,
    "git": help_git,
    "open": help_open,
}
