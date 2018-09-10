#!/usr/bin/env bash
cd $(pwd)
docker-compose run web ./manage.py clearsessions
docker-compose run web ./manage.py thumbnail_cleanup
