#! /usr/bin/env bash

function test_bluer_sandbox_speedtest() {
    if [[ "$BLUER_AI_WEB_IS_ACCESSIBLE" == 0 ]]; then
        bluer_ai_log_warning "web is not accessible, skipping test."
        return
    fi

    if [[ "$abcli_is_github_workflow" == true ]]; then
        bluer_ai_log "test is not available on github, skipping."
        return
    fi

    local options=$1

    bluer_ai_eval ,$options \
        bluer_sandbox_speedtest ~ping
}
