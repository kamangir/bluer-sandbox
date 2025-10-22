#! /usr/bin/env bash

function runme() {
    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_error "rpi not found."
        return 1
    fi

    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        sudo apt install -y python3-bluezero
        pip install bleak
    fi

    # start bluetooth
    sudo systemctl start bluetooth
    sudo systemctl status bluetooth

    sudo hciconfig hci0 up
    hciconfig
}

runme "$@"
