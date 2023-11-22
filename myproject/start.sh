#!/bin/sh

python manage.py migrate
uwsgi --http 0.0.0.0:8000 --module mysite.wsgi --workers 4 --threads 2
