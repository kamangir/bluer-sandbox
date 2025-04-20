#! /usr/bin/env bash

function bluer_sandbox_offline_llm_prompt() {
    local options=$1
    local do_upload=$(bluer_ai_option_int "$options" upload 1)
    local do_tiny=$(bluer_ai_option_int "$options" tiny 0)

    local prompt=$2
    bluer_ai_log "🗣️ $prompt"

    local object_name=$(bluer_ai_clarify_object $3 offline_llm-reply-$(bluer_ai_string_timestamp_short))
    local object_path=$ABCLI_OBJECT_ROOT/$object_name
    mkdir -pv $object_path

    echo "$prompt" >$object_path/prompt.txt

    local model_object_name="offline-llm-model-object"
    local filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf"
    if [[ "$do_tiny" == 1 ]]; then
        filename="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
        model_object_name="$model_object_name-tiny"
    fi

    bluer_ai_log "model: $model_object_name/$filename"

    pushd $abcli_path_git/llama.cpp >/dev/null
    ./build/bin/llama-cli \
        -m $ABCLI_OBJECT_ROOT/$model_object_name/$filename \
        -p "$prompt\n" \
        -n 300 \
        --color \
        --temp 0.7 | tee $object_path/output.txt
    [[ $? -ne 0 ]] && return 1

    popd $abcli_path_git/llama.cpp >/dev/null

    python3 -m bluer_sandbox.offline_llm \
        post_process \
        --object_name $object_name
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    bluer_objects_mlflow_tags_set \
        $object_name \
        contains=offline_llm
}
