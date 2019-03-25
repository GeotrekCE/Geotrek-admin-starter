#!/usr/bin/env bash

DIR="$(dirname "$0")"
cd $DIR

mkdir -p /mnt/backups/geotrek/$(basename $PWD)

source ./.env
export PGPASSWORD=$(echo $POSTGRES_PASSWORD)
pg_dump -Fc --no-acl --no-owner -h 127.0.0.1 -U $POSTGRES_USER $POSTGRES_DB > geotrek_`date +\%Y-\%m-\%d_\%H-\%M`.dump

tar --exclude='*.djcache' --exclude='.git/*' --exclude='*.tar.bz2' --exclude='*.log' --exclude='./var/data/*' --exclude='./var/static/*' --exclude='./var/tiles/*' -cavf /mnt/backups/geotrek/$(basename $PWD)/geotrek_`date +\%Y-\%m-\%d_\%H-\%M`.tar.bz2 .
rm ./geotrek_*.dump
