from typing import List

from bluer_options.terminal import show_usage, xtra


def help_parse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,~upload", mono=mono)

    args = [
        "[--depth <depth>]",
        "[--filename <filename>]",
        "[--root 0]",
    ]

    return show_usage(
        [
            "@parser",
            "parse",
            f"[{options}]",
            "<url>",
            "[-|<object-name>]",
        ]
        + args,
        "parse <url> -> <object-name>.",
        mono=mono,
    )


help_functions = {
    "parse": help_parse,
}
