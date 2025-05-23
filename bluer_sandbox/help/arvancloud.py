from typing import List

from bluer_options.terminal import show_usage, xtra


def help_ssh(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@plugin",
            "node",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "bluer-plugin node <object-name>.",
        mono=mono,
    )


help_functions = {
    "ssh": help_ssh,
}
