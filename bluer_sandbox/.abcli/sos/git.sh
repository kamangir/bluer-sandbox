#! /usr/bin/env bash

function bluer_sandbox_sos_git() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local repo_name=$(bluer_ai_option "$options" repo)

    if [[ ! -z "$repo_name" ]]; then
        local source=$abcli_path_git/$repo_name
        local destination=/Volumes/kamangir/git/$repo_name

        bluer_ai_eval dryrun=$do_dryrun \
            rm -rfv $destination

        bluer_ai_eval dryrun=$do_dryrun \
            cp -Rv \
            $source \
            $destination

        return
    fi

    pushd $abcli_path_git >/dev/null

    for repo_name in $(ls -d */); do
        if [[ ",assets/,assets2/," == *",$repo_name,"* ]]; then
            bluer_ai_log "skipping $repo_name"
            continue
        fi

        bluer_sandbox_sos_git repo=$repo_name,$options
    done

    popd >/dev/null

}
