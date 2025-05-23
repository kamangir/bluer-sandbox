#! /usr/bin/env bash

function bluer_sandbox_arvancloud_ssh() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local pem_filename="~/.ssh/$ARVANCLOUD_PRIVATE_KEY.pem"
    chmod 400 $pem_filename

    bluer_ai_eval dryrun=$do_dryrun \
        ssh \
        -i $pem_filename \
        ubuntu@$ARVANCLOUD_IP
}
