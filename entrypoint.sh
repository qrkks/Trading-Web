#!/bin/ash

echo "Applying migrations..."
python manage.py migrate --no-input

exec "$@"