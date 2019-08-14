#!/usr/bin/env bash

# take care to configure SYNC_RANDO_OPTIONS in custom.py
# This is an example to run docker-compose and launch the command sync_rando :
#<              Docker                   > < Django  > <          Command             >
/usr/local/bin/docker-compose run --rm web ./manage.py sync_rando -v2 /app/src/var/data
