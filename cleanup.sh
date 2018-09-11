#!/usr/bin/env bash
cd $(pwd)
docker exec $(docker ps -q -f name=$(pwd)_web) ./manage.py clearsessions
docker exec $(docker ps -q -f name=$(pwd)_web) ./manage.py thumbnail_cleanup
