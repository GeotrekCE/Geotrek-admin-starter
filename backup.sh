#!/usr/bin/env bash

## This is an example of a backup command, executed every days.

## Get the directory of the actual file (backup.sh)
#DIR="$(dirname "$0")"
#cd $DIR

## Create the backup directory
#mkdir -p /mnt/backups/geotrek/$(basename $PWD)

## Use the datas of connection in .env (could be in other place)
#source ./.env

## Dump the database without owner allowing to change the owner after the restore.
#export PGPASSWORD=$(echo $POSTGRES_PASSWORD)
#pg_dump -Fc --no-acl --no-owner -h 127.0.0.1 -U $POSTGRES_USER $POSTGRES_DB > geotrek_`date +\%Y-\%m-\%d_\%H-\%M`.dump

## Create an archive file of the usefull directories and filesof the application.
#tar --exclude='*.djcache' --exclude='.git/*' --exclude='*.tar.bz2' --exclude='*.log' --exclude='./var/data/*' --exclude='./var/static/*' --exclude='./var/tiles/*' -cavf /mnt/backups/geotrek/$(basename $PWD)/geotrek_`date +\%Y-\%m-\%d_\%H-\%M`.tar.bz2 .

## Remove the dump created just before creating the archive file.
#rm ./geotrek_*.dump
