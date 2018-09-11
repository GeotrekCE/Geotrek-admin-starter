# INSTALL GEOTREK INSTANCE

this file describe how to install geotrek instance on makina geotrek docker server

# Create a specific branch on gitlab geotrek-admin-deploy-docker from master

## Connect to docker server (passwords in vaultier)

```bash
ssh root@ip_of_your_server
```

## Clone and rename folder in /srv/geotrek
```bash
cd /srv/geotrek
git clone https://gitlab.makina-corpus.net/geotrek/geotrek-admin-deploy-docker.git your_instance_name
cd your_instance_name
git checkout -b your_instance_name origin/your_instance_name
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

POSTGRES_HOST=172.17.0.1
POSTGRES_USER=your_database_user
POSTGRES_DB=your_database
POSTGRES_PASSWORD=your_user_password
DOMAIN_NAME=your.final.geotrek.domain
SECRET_KEY=secret-and-unique-secret-and-unique
CONVERSION_HOST=convertit_web
CAPTURE_HOST=screamshotter_web

## Edit custom.py before initial.sh

```bash
$ sudo nano ./var/conf/custom.py
```

Fix at least your :
- SRID
- SPATIAL_EXTENT
- DEFAULT_STRUCTURE_NAME
- MODELTRANSLATION_LANGUAGES

## Launch docker stack
```bash
docker stack deploy -c docker-stack.yml your_instance_name
```

## Test initialize database and basic data

```bash
docker exec $(docker ps -q -f name="your_instance_name_web") initial.sh
```

## Delete instance
```bash
docker stack rm your_instance_name
```

## Redeploy (after update)
```bash
docker stack deploy -c docker-stack.yml your_instance_name
docker exec $(docker ps -q -f name="your_instance_name_web") update.sh
```
