#! /usr/bin/env bash

# internal function
function bluer_sandbox_sos_path() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local source=$2
    local destination=$3

    if [[ -z "$source" ]] || [[ -z "$destination" ]]; then
        bluer_ai_log_error "source/destination not found."
        return 1
    fi

    bluer_ai_log "🆘 $source -> $destination..."

    mkdir -pv $destination

    cp -Rv \
        $source \
        $destination

    echo "$(bluer_ai_string_timestamp) - $source" >>$BLUER_SANDBOX_SOS_PATH/log.txt
}
