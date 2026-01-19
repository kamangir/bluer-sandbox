#! /usr/bin/env bash

function bluer_sandbox_sos_env() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local machine_name=$(bluer_ai_option "$options" rpi)
    if [[ -z "$machine_name" ]]; then
        bluer_ai_log_error "machine name not found."
        return 1
    fi

    bluer_ai_eval dryrun=$do_dryrun \
        scp -r \
        $abcli_path_env_backup \
        pi@$machine_name.local:/home/pi/backup/
}
