# INSTALL GEOTREK

this file describe how to install geotrek instance on makina geotrek docker server

## Create a specific user on server and store password on vaultier

```bash
ssh root@ip_of_your_server
useradd -ms /bin/bash <name_of_your_instance>
passwd <name_of_your_instance>
adduser <name_of_your_instance> sudo
```

## Create user and databse on postgresql server
```bash
$ sudo su
$ su - postgres
$ psql
```

```sql
CREATE USER your_database_user WITH ENCRYPTED PASSWORD 'your_user_password';
CREATE DATABASE your_database WITH OWNER your_database_user;
\c your_database;
CREATE EXTENSION POSTGIS;
```

## Create environment file


```bash
$ cp .env.dist .env
```

## Fill .env with data. If you share postgresql server, you must use docker interface address

```ini
GEOTREK_VERSION=2.19.1
POSTGRES_HOST=172.16.0.1
POSTGRES_USER=your_database_user
POSTGRES_DB=your_database
POSTGRES_PASSWORD=your_user_password
DOMAIN_NAME=your.final.geotrek.domain
SECRET_KEY=secret-and-unique-secret-and-unique
```
## init volume config

```bash
$ docker-compose run web bash exit
```

## Edit custom.py before initial.sh

```bash
$ sudo nano ./var/conf/custom.py
```

Fix at least your :
- SRID
- SPATIAL_EXTENT
- MODELTRANSLATION_LANGUAGES


## Test initialize database and basic data

```bash
$ docker-compose run web initial.sh
```

## Install service

- edit your docker-compose.yml to match with available ports on server
- edit / rename geotrek.nginx.conf with your_instance_name.conf. Fix ports and install in /etc/nginx/sites-availables/. Link to /etc/nginx/sites-enable/
- edit / rename geotrek.systemd.service with your_instance_name.service. Fiw WorkingDirectory to match with your current folder absolute path. Install in /etc/systemd/system/. Activate it with systemctl enable your_instance_name.

## Run
```bash
systemctl start your_instance_name
systemctl stop your_instance_name
```

