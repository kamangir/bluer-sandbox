#! /usr/bin/env bash

function bluer_sandbox_docker() {
    local task=$1

    local function_name=bluer_sandbox_docker_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@docker: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /docker
