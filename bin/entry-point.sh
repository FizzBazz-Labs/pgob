#!/bin/sh

mainDir="/etc/pgob/code"

cd ${mainDir}

pip install -r requirements.txt

echo "Migrate the Database at startup of project"
python manage.py makemigrations
python manage.py migrate

echo "Static command"
python manage.py collectstatic --noinput


echo "Populate the Database at startup of project"
python manage.py loaddata fixtures/db/core.json
python manage.py loaddata fixtures/db/allergies.json
python manage.py loaddata fixtures/db/countries.json
python manage.py loaddata fixtures/db/immunizations.json
python manage.py loaddata fixtures/db/media_channels.json
python manage.py loaddata fixtures/db/medical_histories.json
python manage.py loaddata fixtures/db/positions.json


echo "Init django server"
gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 pgob.wsgi:application

echo "Django docker is fully configured successfully."

exec "$@"
