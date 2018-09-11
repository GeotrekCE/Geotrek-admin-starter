#!/usr/bin/env bash

DIR="$(dirname "$0")"

docker exec $(docker ps -q -f name="$(basename $DIR)"_web) ./manage.py clearsessions
docker exec $(docker ps -q -f name="$(basename $DIR)"_web) ./manage.py thumbnail_cleanup
