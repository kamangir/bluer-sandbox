#! /usr/bin/env bash

function bluer_sandbox_netcat() {
    local task=$1

    local function_name=bluer_sandbox_netcat_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    bluer_ai_log_error "@sandbox: netcat: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /netcat
