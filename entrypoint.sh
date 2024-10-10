#!/bin/sh


while ! pg_isready -h db -p 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done


alembic upgrade head 


if [ "$1" = "pytest" ]; then
    exec "$@"
else
    exec flask run --host=0.0.0.0
fi
