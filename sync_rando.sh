#!/usr/bin/env bash

cd /home/perche/perche-admin

/usr/local/bin/docker-compose run web ./manage.py sync_rando -v2 --url http://geotrek-perche.makina-corpus.net --rando-url http:rando-perche.fr /app/src/var/data
