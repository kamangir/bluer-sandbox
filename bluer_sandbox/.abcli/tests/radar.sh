#! /usr/bin/env bash

function test_bluer_sandbox_radar() {
    local options=$1

    local object_name=test_bluer_sandbox_radar-$(bluer_ai_string_timestamp)

    bluer_ai_eval ,$options \
        bluer_sandbox_radar_fetch \
        ,$options \
        $object_name \
        --max_iteration 5 \
        --seed https://iribnews.ir
}
