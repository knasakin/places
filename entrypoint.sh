#!/bin/bash
sleep 10  # wait for postgres to start up

python manage.py migrate
python manage.py runserver 0.0.0.0:8000