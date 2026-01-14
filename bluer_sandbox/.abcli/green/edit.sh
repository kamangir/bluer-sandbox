#! /usr/bin/env bash

function bluer_sandbox_green_edit() {
    bluer_objects_metadata_edit \
        download,$1 \
        $BLUER_SANDBOX_GREEN_OBJECT_NAME
}
