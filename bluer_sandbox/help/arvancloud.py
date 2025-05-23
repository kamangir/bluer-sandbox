from typing import List

from bluer_options.terminal import show_usage, xtra


def help_ssh(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@arvan",
            "ssh",
            f"[{options}]",
        ],
        "ssh -> arvancloud.",
        mono=mono,
    )


help_functions = {
    "ssh": help_ssh,
}
