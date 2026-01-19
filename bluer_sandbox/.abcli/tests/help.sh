#! /usr/bin/env bash

function test_bluer_sandbox_help() {
    local options=$1

    local module
    for module in \
        "@arvan" \
        "@arvan seed" \
        "@arvan ssh" \
        \
        "@docker" \
        "@docker browse" \
        "@docker build" \
        "@docker clear" \
        "@docker eval" \
        "@docker push" \
        "@docker run" \
        "@docker seed" \
        \
        "@green" \
        "@green edit" \
        "@green review" \
        \
        "@interview" \
        \
        "@llm" \
        "@llm build" \
        "@llm chat" \
        "@llm create_env" \
        "@llm model" \
        "@llm model download" \
        "@llm model get" \
        "@llm prompt" \
        \
        "@netcat" \
        "@netcat connect" \
        "@netcat listen" \
        \
        "@notebooks" \
        "@notebooks build" \
        "@notebooks code" \
        "@notebooks connect" \
        "@notebooks create" \
        "@notebooks host" \
        "@notebooks open" \
        \
        "@radar" \
        "@radar fetch" \
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
        "@sos" \
        "@sos env" \
        "@sos git" \
        \
        "@speedtest" \
        \
        "@tor" \
        "@tor test" \
        "@tor start" \
        \
        "@v2ray" \
        "@v2ray import" \
        "@v2ray install" \
        "@v2ray test" \
        "@v2ray start" \
        \
        "@village" \
        "@village analyze" \
        \
        "bluer_sandbox"; do
        bluer_ai_eval ,$options \
            bluer_ai_help $module
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done

    return 0
}
