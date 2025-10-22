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

        pip install bleak

        # ----
        local bluez_version=5.75
        local tar_filename=bluez-$bluez_version.tar.xz
        local dir_name=bluez-$bluez_version
        bluer_ai_log "upgrading bluez to $bluez_version..."

        pushd $abcli_path_git >/dev/null

        sudo apt remove --purge bluez -y
        sudo apt update
        sudo apt install -y \
            build-essential \
            libdbus-1-dev \
            libglib2.0-dev \
            libudev-dev \
            libical-dev \
            libreadline-dev

        if [[ ! -d "$dir_name" ]]; then
            [[ ! -f "$tar_filename" ]] &&
                wget https://www.kernel.org/pub/linux/bluetooth/$tar_filename

            tar xf $tar_filename
        fi

        cd $dir_name
        ./configure --enable-experimental
        make -j4
        sudo make install
        sudo systemctl restart bluetooth

        bluetoothctl --version

        popd $abcli_path_git >/dev/null

        # --experimental
        bluer_ai_log "turning experimental on ..."

        local service_name=/usr/local/libexec/bluetooth/bluetoothd

        bluer_objects_file \
            sudo \
            replace \
            /lib/systemd/system/bluetooth.service \
            --this "ExecStart=$service_name" \
            --that "ExecStart=$service_name --experimental" \
            --cat $verbose \
            --save 1 \
            --whole_line 1

        sudo systemctl daemon-reexec
        sudo systemctl daemon-reload
        sudo systemctl restart bluetooth

        bluer_ai_log "expecting: $service_name --experimental"
        ps aux | grep bluetoothd
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
