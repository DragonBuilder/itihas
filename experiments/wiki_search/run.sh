#!/bin/bash

export $(xargs < env/dev.env)
poetry run python -m experiments.wiki_search.main