#! /usr/bin/env bash

# internal function to bluer_ai_seed.
function bluer_ai_seed_arvancloud() {
    # seed is NOT local
    seed=$(python3 -m bluer_sandbox.arvancloud generate_seed)
}
