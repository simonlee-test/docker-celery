#!/bin/sh 

echo "Apply database migration mou"

python manage.py migrate

exec "$@"