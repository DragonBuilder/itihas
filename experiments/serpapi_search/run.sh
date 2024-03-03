#!/bin/bash

export $(xargs < env/dev.env)
poetry run python -m experiments.serpapi_search.main