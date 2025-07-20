from typing import List

from bluer_options.terminal import show_usage, xtra


def help_start(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("install", mono=mono)

    return show_usage(
        [
            "@tor",
            "start",
            f"[{options}]",
        ],
        "install tor.",
        mono=mono,
    )


help_functions = {
    "start": help_start,
}
