#! /usr/bin/env bash

function bluer_sandbox_sos_env() {
    local options=$1

    bluer_sandbox_sos_path \
        ,$options \
        $abcli_path_env_backup \
        $BLUER_SANDBOX_SOS_PATH
}
