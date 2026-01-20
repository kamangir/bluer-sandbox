from typing import List

from bluer_options.terminal import show_usage, xtra


def help_fetch(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,upload", mono=mono)

    args = [
        "[--max_iteration <5>]",
        "[--roots 0]",
        "[--seed <url>]",
    ]

    return show_usage(
        [
            "@radar",
            "fetch",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "fetch <url> -> <object-name>.",
        mono=mono,
    )


help_functions = {
    "fetch": help_fetch,
}
