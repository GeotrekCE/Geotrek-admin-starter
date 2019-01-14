#!/usr/bin/env bash

DIR="$(dirname "$0")"
cd $DIR

/usr/local/bin/docker-compose exec -T web ./manage.py clearsessions
/usr/local/bin/docker-compose exec -T web ./manage.py thumbnail_cleanup
