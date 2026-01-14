#! /usr/bin/env bash

function bluer_sandbox_green() {
    local task=$1

    local function_name=bluer_sandbox_green_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 bluer_sandbox.green "$@"
}

bluer_ai_source_caller_suffix_path /green
