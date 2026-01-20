#! /usr/bin/env bash

function bluer_sandbox_sos_git() {
    local options=$1
    local repo_name=$(bluer_ai_option "$options" repo)

    if [[ ! -z "$repo_name" ]]; then
        bluer_sandbox_sos_path \
            ,$options \
            $abcli_path_git/$repo_name \
            $BLUER_SANDBOX_SOS_PATH/git/

        return
    fi

    pushd $abcli_path_git >/dev/null

    for repo_name in $(ls -d */); do
        repo_name=${repo_name%/}
        if [[ "$repo_name" == assets* ]]; then
            bluer_ai_log "skipping $repo_name"
            continue
        fi

        bluer_sandbox_sos_git repo=$repo_name,$options
    done

    popd >/dev/null

}
