#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# 1. Wipe the bad data that is causing the foreign key conflict
python manage.py shell -c "from academy.models import Material; Material.objects.all().delete()"

# 2. Tell Django to forget the broken migration history for the academy app
python manage.py migrate academy zero --fake

# 3. Run migrations fresh so the 'Course' table and 'course_id' column are actually created
python manage.py migrate academy

# 4. Run remaining migrations and collect static files
python manage.py migrate
python manage.py collectstatic --no-input