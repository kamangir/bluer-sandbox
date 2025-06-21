#! /usr/bin/env bash

function test_bluer_sandbox_parser_parse() {
    local options=$1

    local object_name=test_bluer_sandbox_parser_parse-$(bluer_ai_string_timestamp)

    bluer_ai_eval ,$options \
        bluer_sandbox_parser_parse \
        ~upload,$options \
        https://iribnews.ir \
        $object_name
}
