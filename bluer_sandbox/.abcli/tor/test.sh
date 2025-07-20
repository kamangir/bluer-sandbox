#! /usr/bin/env bash

function bluer_sandbox_tor_check() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    bluer_ai_eval dryrun=$do_dryrun \
        curl \
        --socks5-hostname 127.0.0.1:9050 \
        https://check.torproject.org/api/ip
}
