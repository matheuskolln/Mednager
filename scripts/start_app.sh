#!/usr/bin/bash

echo "Building container"
docker-compose build
docker-compose up -d db

echo "Checking MySQL"
docker-compose exec -T db mysqladmin ping -h localhost -P 3306 --protocol tcp -uroot -proot --silent

# Wait for MySQL to start
while ! docker-compose exec -T db mysqladmin ping -h localhost -P 3306 --protocol tcp -uroot -proot --silent; do
    sleep 1
done

echo "Making migrations"
docker-compose run backend alembic upgrade head

echo "Starting application"
docker-compose up
