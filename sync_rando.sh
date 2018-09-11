#!/usr/bin/env bash

cd $(pwd)

docker exec $(docker ps -q -f name=$(pwd)_web) ./manage.py sync_rando -v2 /app/src/var/data
