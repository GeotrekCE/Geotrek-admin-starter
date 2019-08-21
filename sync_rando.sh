#!/usr/bin/env bash



DIR="$(dirname "$0")"
cd $DIR
# sync_rando logs in var/log/sync_rando.log
LOG_FILE=$DIR/var/log/sync_rando.log

date > $LOG_FILE

echo "Run parsers Tourinsoft imports" >> $LOG_FILE

# take care to configure SYNC_RANDO_OPTIONS in custom.py
# This is an example to run docker-compose and launch the command sync_rando :
#<              Docker                   > < Django  > <          Command             > <     log_file        >
/usr/local/bin/docker-compose run --rm web ./manage.py sync_rando -v2 /app/src/var/data 2>&1 | tee -a $LOG_FILE
