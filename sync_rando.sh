#!/usr/bin/env bash

/usr/local/bin/docker-compose run web ./manage.py sync_rando -v2 --url http://admin.geotrek.fr --rando-url http://rando.geotrek.fr /app/src/var/data
