#!/usr/bin/env bash

# must be run inside docker-compose directory

source ./.env
export PGPASSWORD=$(echo $POSTGRES_PASSWORD)
pg_dump -Fc --no-acl --no-owner -h 127.0.0.1 -U $POSTGRES_USER $POSTGRES_DB > geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.dump

tar --exclude='*.djcache'  --exclude='*.tgz' --exclude='*.log' -zcvf /var/backups/geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.tgz .
rm geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.dump
