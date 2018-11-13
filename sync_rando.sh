#!/usr/bin/env bash

# take care to configure SYNC_RANDO_OPTIONS in custom.py
docker-compose exec web ./manage.py sync_rando -v2 /app/src/var/data
