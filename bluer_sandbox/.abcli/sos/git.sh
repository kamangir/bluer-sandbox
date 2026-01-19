#! /usr/bin/env bash

function bluer_sandbox_sos_git() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local machine_name=$(bluer_ai_option "$options" rpi)
    if [[ -z "$machine_name" ]]; then
        bluer_ai_log_error "machine name not found."
        return 1
    fi

    local repo_name=$(bluer_ai_option "$options" repo)

    local source=$abcli_path_git
    local destination=/home/pi/backup
    if [[ ! -z "$repo_name" ]]; then
        source=$source/$repo_name
        destination=$destination/git/$repo_name
    fi

    bluer_ai_eval dryrun=$do_dryrun \
        scp -r \
        $source \
        pi@$machine_name.local:$destination
}
