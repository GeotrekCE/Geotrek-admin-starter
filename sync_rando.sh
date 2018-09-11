#!/usr/bin/env bash
DIR="$(dirname "$0")"

docker exec $(docker ps -q -f name=$(basename $DIR)_web) ./manage.py sync_rando -v2 /app/src/var/data
