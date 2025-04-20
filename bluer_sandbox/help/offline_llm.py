from typing import List

from bluer_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@offline_llm",
            "install",
            f"[{options}]",
        ],
        "install offline_llm.",
        mono=mono,
    )


def help_model_get(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "tiny"

    options_what = "filename | object | repo"

    return show_usage(
        [
            "@offline_llm",
            "model",
            "get",
            f"[{options}]",
            f"[{options_what}]",
        ],
        "get things.",
        mono=mono,
    )


def help_model_download(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,overwrite,tiny", mono=mono)

    return show_usage(
        [
            "@offline_llm",
            "model",
            "download",
            f"[{options}]",
        ],
        "download the model.",
        mono=mono,
    )


def help_prompt(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("tiny,~upload", mono=mono)

    return show_usage(
        [
            "@offline_llm",
            "prompt",
            f"[{options}]",
            '"<prompt>"',
            "[-|<object-name>]",
        ],
        '"<prompt>" -> offline_llm.',
        mono=mono,
    )


help_functions = {
    "install": help_install,
    "model": {
        "download": help_model_download,
        "get": help_model_get,
    },
    "prompt": help_prompt,
}
