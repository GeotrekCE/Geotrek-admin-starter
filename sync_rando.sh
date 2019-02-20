#!/usr/bin/env bash

# take care to configure SYNC_RANDO_OPTIONS in custom.py
/usr/local/bin/docker-compose run --rm web ./manage.py sync_rando -v2 /app/src/var/data
