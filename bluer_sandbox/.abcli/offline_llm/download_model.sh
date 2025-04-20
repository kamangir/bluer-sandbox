#! /usr/bin/env bash

# https://chatgpt.com/c/68046861-c950-8005-8f01-a2c27754b4b5
function bluer_sandbox_offline_llm_download_model() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_tiny=$(bluer_ai_option_int "$options" tiny 0)
    local overwrite=$(bluer_ai_option_int "$options" overwrite 0)

    local model_object_name="offline-llm-model-object"
    [[ "$do_tiny" == 1 ]] &&
        model_object_name="$model_object_name-tiny"

    local model_object_path=$ABCLI_OBJECT_ROOT/$model_object_name
    mkdir -pv $model_object_path

    local repo_name="TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
    local filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf"
    if [[ "$do_tiny" == 1 ]]; then
        repo_name="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
        filename="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    fi

    if [[ "$overwrite" == 0 ]] && [[ -f "$model_object_path/$filename" ]]; then
        bluer_ai_log "✅ $repo_name/$filename"
        return 0
    fi
    bluer_ai_log "downloading $repo_name/$filename -> $model_object_path ..."

    bluer_ai_eval dryrun=$do_dryrun \
        huggingface-cli download $repo_name \
        $filename \
        --local-dir $model_object_path \
        --local-dir-use-symlinks False
}
