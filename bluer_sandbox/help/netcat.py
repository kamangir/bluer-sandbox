from typing import List

from bluer_options.terminal import show_usage, xtra


def help_connect(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "ip=<IP>",
            xtra(",port=<port>", mono=mono),
        ]
    )

    return show_usage(
        [
            "@netcat",
            "connect",
            f"[{options}]",
        ],
        "connect to netcat.",
        mono=mono,
    )


def help_listen(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("port=<port>", mono=mono)

    return show_usage(
        [
            "@netcat",
            "listen",
            f"[{options}]",
        ],
        "listen to netcat.",
        mono=mono,
    )


help_functions = {
    "connect": help_connect,
    "listen": help_listen,
}
