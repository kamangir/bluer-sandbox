from typing import List

from bluer_options.terminal import show_usage, xtra


def help_edit(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download", mono=mono)

    return show_usage(
        [
            "@green",
            "edit",
            f"[{options}]",
        ],
        "edit green db.",
        mono=mono,
    )


def help_review(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download,~upload", mono=mono)

    return show_usage(
        [
            "@green",
            "review",
            f"[{options}]",
        ],
        "review green db.",
        mono=mono,
    )


help_functions = {
    "edit": help_edit,
    "review": help_review,
}
