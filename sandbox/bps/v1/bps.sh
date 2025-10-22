#! /usr/bin/env bash

function runme() {
    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_error "rpi not found."
        return 1
    fi

    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 1)
    local do_start=$(bluer_ai_option_int "$options" start 1)

    if [[ "$do_install" == 1 ]]; then
        sudo apt update
        sudo apt install -y \
            bluez \
            python3-dbus \
            python3-gi \
            libglib2.0-dev \
            libcairo2-dev \
            pkg-config \
            cmake

        pip3 install bluezero
        python3 -c "import bluezero; print(bluezero.__version__)"

        pip install bleak
    fi

    if [[ "$do_start" == 1 ]]; then
        sudo systemctl start bluetooth
        sudo systemctl status bluetooth

        sudo hciconfig hci0 up
        hciconfig
    fi
}

runme "$@"
