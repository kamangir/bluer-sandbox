#! /usr/bin/env bash

function test_bluer_sandbox_speedtest() {
    if [[ "$BLUER_AI_WEB_STATUS" != online ]]; then
        bluer_ai_log_warning "internet is not online, test is disabled."
        return
    fi

    local options=$1

    bluer_ai_eval ,$options \
        bluer_sandbox_speedtest ~ping
}
