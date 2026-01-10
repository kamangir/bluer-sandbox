#! /usr/bin/env bash

function bluer_sandbox_netcat_connect() {
    local options=$1
    local ip=$(bluer_ai_option "$options" ip)
    local port=$(bluer_ai_option "$options" port $BLUER_SANDBOX_NETCAT_DEFAULT_PORT)

    if [[ -z "$ip" ]]; then
        bluer_ai_log_error "ip not found."
        return 1
    fi

    bluer_ai_eval - \
        nc $ip $port
}
