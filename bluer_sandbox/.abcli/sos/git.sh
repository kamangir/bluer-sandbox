#! /usr/bin/env bash

function bluer_sandbox_sos_git() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local repo_name=$(bluer_ai_option "$options" repo)

    local source=$abcli_path_git
    local destination=/Volumes/kamangir/git
    if [[ ! -z "$repo_name" ]]; then
        source=$source/$repo_name
        destination=$destination/$repo_name
    fi

    rm -rfv $destination

    bluer_ai_eval dryrun=$do_dryrun \
        cp -Rv \
        $source \
        $destination
}
