#! /usr/bin/env bash

function bluer_sandbox_netcat_listen() {
    local options=$1
    local port=$(bluer_ai_option "$options" port $BLUER_SANDBOX_NETCAT_DEFAULT_PORT)

    bluer_ai_log "type in \"@netcat connect ip=$BLUER_AI_IP\" to connect."

    bluer_ai_eval - \
        nc -l $port
}
