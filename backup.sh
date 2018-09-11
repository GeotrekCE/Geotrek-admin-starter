#!/usr/bin/env bash
PWD="$(pwd)"
cd $PWD

source ./.env
export PGPASSWORD=$(echo $POSTGRES_PASSWORD)
pg_dump -Fc --no-acl --no-owner -h 127.0.0.1 -U $POSTGRES_USER $POSTGRES_DB > geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.dump

mkdir -p /var/backups/geotrek/$(basename $PWD)

tar --exclude='*.djcache'  --exclude='*.tgz' --exclude='*.log' --exclude='*.dump' --exclude='./var/data/*' --exclude='./var/static/*' --exclude='./var/tiles/*' -zcvf /var/backups/geotrek/$(basename $PWD)/geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.tgz .
rm geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.dump
