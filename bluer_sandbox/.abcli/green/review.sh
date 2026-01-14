#! /usr/bin/env bash

function bluer_sandbox_green_review() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_upload=$(bluer_ai_option_int "$options" upload 1)

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - $BLUER_SANDBOX_GREEN_OBJECT_NAME

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_sandbox.green \
        review \
        --object_name $BLUER_SANDBOX_GREEN_OBJECT_NAME \
        "${@:2}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $BLUER_SANDBOX_GREEN_OBJECT_NAME

    return $status
}
