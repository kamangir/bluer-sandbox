#! /usr/bin/env bash

function runme() {
    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        if [[ "$abcli_is_rpi" == false ]]; then
            bluer_ai_log_error "install only runs on rpi."
            return 1
        fi

        sudo apt install -y python3-bluezero
        pip install bleak
        sudo systemctl start bluetooth
        sudo hciconfig hci0 up
    fi

}

runme "$@"
