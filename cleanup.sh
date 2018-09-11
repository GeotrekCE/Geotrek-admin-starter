#!/usr/bin/env bash

PWD="$(pwd)"

docker exec $(docker ps -q -f name="$(basename $PWD)"_web) ./manage.py clearsessions
docker exec $(docker ps -q -f name="$(basename $PWD)"_web) ./manage.py thumbnail_cleanup
