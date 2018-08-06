#!/usr/bin/env bash

cd /home/arche-agglo/arche-agglo-admin

/usr/local/bin/docker-compose run web ./manage.py sync_rando -v2 --url http://geotrek-ardeche-hermitage.fr --rando-url http://rando-ardeche-hermitage.fr /app/src/var/data
