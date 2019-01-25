#!/bin/bash -e

# This script requires several environmental variables to be set to deploy. Note that if the
# users already exist in SEED or Postgres then they will not be recreated and their passwords
# will not be updated.

: << 'arguments'
There is only one optional argument and that is the name of the docker compose file to load.
For example: ./deploy.sh docker-compose.local.oep.yml

There are several required environment variables that need to be set in order to launch seed:
POSTGRES_DB (optional), defaults to seed
DJANGO_SETTINGS_MODULE (optional), defaults to config.settings.docker
POSTGRES_USER (required), admin user of postgres database
POSTGRES_PASSWORD (required), admin password for postgres database
SEED_ADMIN_USER (required), admin user for SEED
SEED_ADMIN_PASSWORD (required), admin password for SEED
SEED_ADMIN_ORG (required), default organization for admin user in SEED
SECRET_KEY (required), unique key for SEED web application
AWS_ACCESS_KEY (optional), Access key for AWS
AWS_SECRET_ACCESS_KEY, Secret key for AWS
AWS_SES_REGION_NAME (optional), AWS Region for SES
AWS_SES_REGION_ENDPOINT (optional), AWS endpoint for SES
SERVER_EMAIL (optional), Email that is used by the server to send messages

# example (do not use these values in production).
export POSTGRES_USER=seed
export POSTGRES_PASSWORD=super-secret-password
export SEED_ADMIN_USER=user@seed-platform.org
export SEED_ADMIN_PASSWORD=super-secret-password
export SEED_ADMIN_ORG=default
export SECRET_KEY=ARQV8qGuJKH8sGnBf6ZeEdJQRKLTUhsvEcp8qG9X9sCPXvGLhdxqnNXpZcy6HEyf
# If using SES for email, then you need to also pass in the following optional arguments (change as
# needed):
export AWS_ACCESS_KEY_ID=key
export AWS_SECRET_ACCESS_KEY=secret_key
export AWS_SES_REGION_NAME=us-west-2
export AWS_SES_REGION_ENDPOINT=email.us-west-2.amazonaws.com
export SERVER_EMAIL=info@seed-platform.org
arguments

# Verify that env vars are set
if [ -z ${POSTGRES_USER+x} ]; then
    echo "POSTGRES_USER is not set"
    exit 1
fi

if [ -z ${POSTGRES_PASSWORD+x} ]; then
    echo "POSTGRES_PASSWORD is not set"
    exit 1
fi

if [ -z ${SEED_ADMIN_USER+x} ]; then
    echo "SEED_ADMIN_USER is not set"
    exit 1
fi

if [ -z ${SEED_ADMIN_USER+x} ]; then
    echo "SEED_ADMIN_USER is not set"
    exit 1
fi

if [ -z ${SEED_ADMIN_PASSWORD+x} ]; then
    echo "SEED_ADMIN_PASSWORD is not set"
    exit 1
fi

if [ -z ${SEED_ADMIN_ORG+x} ]; then
    echo "SEED_ADMIN_PASSWORD is not set"
    exit 1
fi

if [ -z ${SECRET_KEY+x} ]; then
    echo "SECRET_KEY is not set"
    exit 1
fi

DOCKER_COMPOSE_FILE=docker-compose.local.yml
if [ -z "$1" ]; then
    echo "There are no arguments, defaulting to use '${DOCKER_COMPOSE_FILE}'."
else
    DOCKER_COMPOSE_FILE=$1
    echo "Using passed docker-compose file of ${DOCKER_COMPOSE_FILE}"
fi

if docker exec $(docker ps -qf "name=registry") true > /dev/null 2>&1; then
    echo "Registry is already running"
else
    echo "Creating registry"
    docker volume create --name=regdata
    docker service create --name registry --publish 5000:5000 --mount type=volume,source=regdata,destination=/var/lib/registry registry:2.6
fi

if docker node ls > /dev/null 2>&1; then
  echo "Swarm already initialized"
else
  docker swarm init
fi

echo "Building lasest version of SEED"
# explicitly pull images from docker-compose. Note that you will need to keep the
# versions consistent between the compose file and what is below.
docker-compose pull
docker-compose build

echo "Tagging local containers"
docker tag seedplatform/seed:latest 127.0.0.1:5000/seed
docker tag postgres:11.1 127.0.0.1:5000/postgres
docker tag redis:5.0.1 127.0.0.1:5000/redis
docker tag seedplatform/oep:1.0.0-SNAPSHOT 127.0.0.1:5000/oep

sleep 3
echo "Pushing tagged versions to local registry"
docker push 127.0.0.1:5000/seed
docker push 127.0.0.1:5000/postgres
docker push 127.0.0.1:5000/redis
docker push 127.0.0.1:5000/oep

echo "Deploying"
# check if the stack is running, and if so then shut it down
docker stack deploy seed --compose-file=${DOCKER_COMPOSE_FILE} &
wait $!
while ( nc -zv 127.0.0.1 80 3>&1 1>&2- 2>&3- ) | awk -F ":" '$3 != " Connection refused" {exit 1}'; do echo -n "."; sleep 5; done
echo 'SEED stack redeployed'

echo "Waiting for webserver to respond"
until curl -sf --output /dev/null "127.0.0.1"; do echo -n "."; sleep 1; done
