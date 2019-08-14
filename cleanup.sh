#!/usr/bin/env bash

# Cleanup all the sessions and thumbnail not used
DIR="$(dirname "$0")"
cd $DIR

/usr/local/bin/docker-compose exec -T web ./manage.py clearsessions
/usr/local/bin/docker-compose exec -T web ./manage.py thumbnail_cleanup
/usr/local/bin/docker-compose exec -T web ./manage.py remove_thumbnails