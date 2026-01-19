#! /usr/bin/env bash

function bluer_sandbox_sos() {
    local task=$1

    local function_name=bluer_sandbox_sos_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    local task
    for task in env git; do
        bluer_sandbox_sos_${task} "$@"
        [[ $? -ne 0 ]] && return 1
        bluer_ai_hr
    done
}

bluer_ai_source_caller_suffix_path /sos
