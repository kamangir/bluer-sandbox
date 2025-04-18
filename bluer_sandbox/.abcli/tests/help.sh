#! /usr/bin/env bash

function test_bluer_sandbox_help() {
    local options=$1

    local module
    for module in \
        "@assets" \
        "@assets publish" \
        \
        "@notebooks" \
        "@notebooks open" \
        "@notebooks build" \
        "@notebooks code" \
        "@notebooks connect" \
        "@notebooks create" \
        "@notebooks host" \
        \
        "@offline_llm" \
        "@offline_llm install" \
        "@offline_llm prompt" \
        \
        "@sandbox" \
        \
        "@sandbox pypi" \
        "@sandbox pypi browse" \
        "@sandbox pypi build" \
        "@sandbox pypi install" \
        \
        "@sandbox pytest" \
        \
        "@sandbox test" \
        "@sandbox test list" \
        \
        "bluer_sandbox"; do
        bluer_ai_eval ,$options \
            bluer_ai_help $module
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done

    return 0
}
