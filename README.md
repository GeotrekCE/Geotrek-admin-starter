# INSTALL GEOTREK INSTANCE

This file describe how to install geotrek.

## Clone the folder
```bash
mkdir -p geotrek
cd geotrek
git clone https://github.com/GeotrekCE/Geotrek-admin-starter.git .
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

## Fill .env with data. If you share postgresql server, you must use <docker interface> address

```
GEOTREK_VERSION=geotrek_version
POSTGRES_HOST=<172.17.0.1> ( | interface_address)
POSTGRES_USER=your_database_user
POSTGRES_DB=your_database
POSTGRES_PASSWORD=your_user_password
DOMAIN_NAME=your.final.geotrek.domain
SECRET_KEY=secret-and-unique-secret-and-unique
GUNICORN_CMD_ARGS=--bind=0.0.0.0:8000 --workers=5 --timeout=600
# CONVERSION_HOST=convertit_web
# CAPTURE_HOST=screamshotter_web
```
For the version of geotrek check : https://geotrek.readthedocs.io/en/master/changelog.html
It can't be bellow 2.19.0


## Init volume config

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
```bash
docker-compose run web initial.sh
```
___________________________
___________________________

## Install Service

1. Create a symbolic link between your nginx and /etc/nginx/sites-enabled/
    ```bash
    mkdir /var/www/geotrek -p  # This path has to correspond with your root in nginx.conf
    ln -s geotrek/var/media /var/www/geotrek
    ln -s geotrek/var/static /var/www/geotrek
    ln -s nginx.conf /etc/nginx/sites-enabled/geotrek.conf
    ```
2. Fix Working Directory in geotrek.service
    ```
    WorkingDirectory=<path of geotrek>  # You can use the command : $ pwd
    ```
3. Copy your service in /etc/systemd/system
    ```bash
    cp geotrek.service /etc/systemd/system/geotrek.service
    ```
4. Enable the system
    ```bash
    systemctl enable geotrek.service
    ```

## Run or Stop the service
```bash
systemctl start geotrek
systemctl stop geotrek
```

## CRON jobs

### Backup

edit host's cron to run backup.sh

### Sync rando

edit host's cron to run sync_rando.sh

Don't forget to set SYNC_RANDO_OPTIONS in custom.py to set url, portal_url, skip_tiles and other required sync settings

### Parsers

edit host's cron to run
