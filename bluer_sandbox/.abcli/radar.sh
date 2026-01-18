#! /usr/bin/env bash

function bluer_sandbox_radar() {
    local task=$1

    local function_name=bluer_sandbox_radar_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_sandbox.radar "$@"
}

bluer_ai_source_caller_suffix_path /radar
