#!/bin/bash

echo "Applying database migrations"
python manage.py migrate

# collect static files
python manage.py collectstatic --noinput

# run server
python manage.py runserver 0.0.0.0:8000
