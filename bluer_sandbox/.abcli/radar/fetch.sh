#! /usr/bin/env bash

function bluer_sandbox_radar_fetch() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_upload=$(bluer_ai_option_int "$options" upload $(bluer_ai_not $do_dryrun))

    local url=${2:-$BLUER_AI_NATIONAL_INTERNAT_INDEX}

    local object_name=$(bluer_ai_clarify_object $3 fetch-$(bluer_ai_string_timestamp))

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_sandbox.radar \
        fetch \
        --url $url \
        --object_name $object_name \
        "${@:4}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return 0
}
