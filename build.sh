#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# 1. DROP the academy tables entirely to fix the column mismatch
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute('DROP TABLE IF EXISTS academy_material CASCADE; DROP TABLE IF EXISTS academy_course CASCADE; DROP TABLE IF EXISTS academy_programme CASCADE; DROP TABLE IF EXISTS academy_department CASCADE; DROP TABLE IF EXISTS academy_school CASCADE;')"

# 2. CLEAR the migration history for the academy app
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute(\"DELETE FROM django_migrations WHERE app='academy'\")"

# 3. Now run the migrations for real (No Faking)
python manage.py migrate academy

# 4. Finish the rest
python manage.py migrate
python manage.py collectstatic --no-input