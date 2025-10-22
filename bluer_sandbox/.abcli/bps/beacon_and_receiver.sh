#! /usr/bin/env bash

function bluer_sandbox_bps_beacon_and_receiver() {
    sudo systemctl restart bluetooth

    bluer_ai_eval ,$1 \
        python3 -m \
        bluer_sandbox.bps.utils.beacon_and_receiver \
        "${@:2}"
}
