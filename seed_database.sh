#!/bin/bash

rm db.sqlite3
rm -rf ./capstoneApi/migrations
python3 manage.py migrate
python3 manage.py makemigrations capstoneApi
python3 manage.py migrate capstoneApi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata hosts
python3 manage.py loaddata guests
python3 manage.py loaddata buses
python3 manage.py loaddata reservations
python3 manage.py loaddata rentals