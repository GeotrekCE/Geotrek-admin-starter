# INSTALL GEOTREK INSTANCE

This file describe how to install geotrek.

## Clone the folder
```bash
cd /srv/geotrek
git clone geotrek https://github.com/GeotrekCE/Geotrek-admin-starter.git
cd geotrek
```

## Create user and database on postgresql server
```bash
$ su - postgres
$ psql
```

```sql
CREATE USER your_database_user WITH ENCRYPTED PASSWORD 'your_user_password';
CREATE DATABASE your_database WITH OWNER your_database_user;
\c your_database
CREATE EXTENSION POSTGIS;
\q
```

## Create environment file


```bash
$ cp .env.dist .env
```

## Fill .env with data. If you share postgresql server, you must use docker interface address

```
GEOTREK_VERSION=geotrek_version
POSTGRES_HOST=172.17.0.1 ( | interface_address)
POSTGRES_USER=your_database_user
POSTGRES_DB=your_database
POSTGRES_PASSWORD=your_user_password
DOMAIN_NAME=your.final.geotrek.domain
SECRET_KEY=secret-and-unique-secret-and-unique
GUNICORN_CMD_ARGS=--bind=0.0.0.0:8000 --workers=5 --timeout=600
# CONVERSION_HOST=convertit_web
# CAPTURE_HOST=screamshotter_web
```
For the version of geotrek check : https://hub.docker.com/r/geotrekce/admin/tags/

## Init volume config (with docker-compose)

```bash
docker-compose run web bash exit
```

## Edit custom.py before initial.sh

```bash
$ sudo nano ./var/conf/custom.py
```

Fix at least your :
- SRID
- SPATIAL_EXTENT
- DEFAULT_STRUCTURE_NAME
- MODELTRANSLATION_LANGUAGES
- SYNC_RANDO_OPTIONS

## Test initialize database and basic data
_With docker-compose :_
```bash
docker-compose run web initial.sh
```
___________________________
___________________________

## Install Service

1. Create a symbolic link between your nginx and /etc/nginx/sites-enable/
    ```bash
    ln -s nginx.conf /etc/nginx/sites-enable/geotrek.conf
    ```
2. Rename your service :
    ```bash
    mv your_instance_name.service geotrek.service
    ```
3. Fix Working Directory in <your_instance_name>.service
    ```
    WorkingDirectory=/your_directory/
    ```
4. Copy your service in /etc/systemd/system
    ```bash
    cp geotrek.service /etc/systemd/system/geotrek.service
    ```
5. Enable the system
    ```bash
    systemctl enable geotrek.service
    ```

## Run or Stop the service
```bash
systemctl start your_instance_name
systemctl stop your_instance_name
```

## CRON jobs

### Cleanup

edit host's cron to run cleanup.sh

### Backup

edit host's cron to run backup.sh
Backup are stored in /var/backups/geotrek/your_instance_name

### Sync rando

edit host's cron to run sync_rando.sh

Don't forget to set SYNC_RANDO_OPTIONS in custom.py to set url, portal_url, skip_tiles and other required sync settings

### Parsers

edit host's cron to run 