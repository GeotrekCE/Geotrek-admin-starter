#!/usr/bin/env bash

cd $(pwd)

/usr/local/bin/docker-compose run web ./manage.py sync_rando -v2 /app/src/var/data
