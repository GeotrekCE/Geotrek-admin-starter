#!/usr/bin/env bash

cd /home/perche/perche-admin

source ./.env
export PGPASSWORD=$(echo $POSTGRES_PASSWORD)
final_name = geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.dump
pg_dump -Fc --no-acl --no-owner -h 127.0.0.1 -U $POSTGRES_USER $POSTGRES_DB > $final_name

tar --exclude='*.djcache'  --exclude='*.tgz' --exclude='*.log' -zcvf /var/backups/geotrek/perche/geotrek_`date +\%Y-\%m-\%d_\%H:\%M`.tgz .
rm $final_name
