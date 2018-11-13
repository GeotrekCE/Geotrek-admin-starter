#!/usr/bin/env bash

docker-compose exec web ./manage.py clearsessions
docker-compose exec web ./manage.py thumbnail_cleanup
