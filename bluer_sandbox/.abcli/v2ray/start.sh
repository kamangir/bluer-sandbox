#! /usr/bin/env bash

function bluer_sandbox_v2ray_start() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        bluer_ai_log 🪄
    fi

    bluer_sandbox_v2ray_test $options
}
