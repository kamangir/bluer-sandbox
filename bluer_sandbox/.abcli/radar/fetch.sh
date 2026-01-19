#! /usr/bin/env bash

function bluer_sandbox_radar_fetch() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    local object_name=$(bluer_ai_clarify_object $2 fetch-$(bluer_ai_string_timestamp))

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - $object_name

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_sandbox.radar \
        fetch \
        --object_name $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return 0
}
