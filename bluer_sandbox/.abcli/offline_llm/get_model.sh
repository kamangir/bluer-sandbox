#! /usr/bin/env bash

function bluer_sandbox_offline_llm_model_get() {
    local options=$1
    local do_tiny=$(bluer_ai_option_int "$options" tiny 0)

    local options_what=$1
    local what=$(bluer_ai_option_choice "$options_what" filename,object,repo object)

    if [[ "$what" == object ]]; then
        local model_object_name="offline-llm-model-object"
        [[ "$do_tiny" == 1 ]] &&
            model_object_name="$model_object_name-tiny"

        echo $model_object_name
        return
    fi

    :
}
