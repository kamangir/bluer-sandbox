#! /usr/bin/env bash

function runme() {
    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_error "rpi not found."
        return 1
    fi

    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)
    local do_start=$(bluer_ai_option_int "$options" start 1)
    local what=$(bluer_ai_option_choice "$options" beacon,receiver,beacon+receiver beacon+receiver)
    local verbose=$(bluer_ai_option_int "$options" verbose 1)

    if [[ "$do_install" == 1 ]]; then
        bluer_ai_log "installing ..."

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
        pip install dbus-next

        pip install bleak

        # ----
        bluer_ai_log "installing bluez ..."
        sudo apt install --reinstall bluez -y

        # --experimental
        bluer_ai_log "turning experimental on ..."

        sudo mkdir -pv /etc/systemd/system/bluetooth.service.d

        sudo cp -v \
            ./override.conf \
            /etc/systemd/system/bluetooth.service.d/override.conf

        sudo systemctl daemon-reexec
        sudo systemctl daemon-reload

        sudo systemctl restart bluetooth

        ps -eo args | grep [b]luetoothd
    fi

    if [[ "$do_start" == 1 ]]; then
        bluer_ai_log "starting bluetooth..."

        sudo systemctl start bluetooth
        sudo systemctl status --no-pager bluetooth

        sudo bluetoothctl power on
        sudo bluetoothctl discoverable on
        bluer_ai_eval - \
            sudo bluetoothctl show
    fi

    bluer_ai_log "starting $what ..."
    if [[ "$what" == "beacon" ]]; then
        python3 beacon.py
    elif [[ "$what" == "receiver" ]]; then
        sudo hcitool lescan
    elif [[ "$what" == "beacon+receiver" ]]; then
        python3 bps.py
    else
        bluer_ai_log_error "cannot start $what."
    fi
}

runme "$@"
