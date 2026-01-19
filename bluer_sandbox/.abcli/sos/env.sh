#! /usr/bin/env bash

function bluer_sandbox_sos_env() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local destination=/Volumes/kamangir/env

    rm -rfv $destination

    bluer_ai_eval dryrun=$do_dryrun \
        cp -Rv \
        $abcli_path_env_backup \
        $destination
}
