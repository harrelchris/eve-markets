#!/usr/bin/env bash

source .venv/bin/activate

black app --line-length 120 --extend-exclude='^(.*/)?(migrations|fixtures)/'

flake8 app --max-line-length 120 --extend-exclude .idea/,.venv/,*/migrations/

isort app --profile black --line-length 120 --src-path app
