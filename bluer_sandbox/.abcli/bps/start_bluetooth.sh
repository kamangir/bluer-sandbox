#! /usr/bin/env bash

function bluer_sandbox_bps_start_bluetooth() {
    local options=$1
    local verbose=$(bluer_ai_option_int "$options" verbose 0)

    bluer_ai_log "starting bluetooth..."

    sudo systemctl start bluetooth
    [[ "$verbose" == 1 ]] &&
        bluer_ai_eval - \
            sudo systemctl status \
            --no-pager bluetooth

    sudo bluetoothctl power on
    sudo bluetoothctl discoverable on

    [[ "$verbose" == 1 ]] &&
        bluer_ai_eval - \
            sudo bluetoothctl show

    return 0
}
