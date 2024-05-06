# Pgob

## Dump data

```bash
python manage.py dumpdata core -o fixtures/db/core.json
```

## Load Data

```bash
python manage.py loaddata fixtures/db/groups.json & \
python manage.py loaddata fixtures/db/accreditations.json & \
python manage.py loaddata fixtures/db/allergies.json & \
python manage.py loaddata fixtures/db/countries.json & \
python manage.py loaddata fixtures/db/immunizations.json & \
python manage.py loaddata fixtures/db/media_channels.json & \
python manage.py loaddata fixtures/db/medical_histories.json & \
python manage.py loaddata fixtures/db/positions.json
```
