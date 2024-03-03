#!/bin/bash

exp_name=$1

if [[ -z "$exp_name" ]]; then
    echo "no experiment name provided"
    echo "usage: ./run_experiment.sh <experiment_name>"
    exit 1
fi

export $(xargs < env/dev.env)
poetry run python -m experiments.$exp_name.main