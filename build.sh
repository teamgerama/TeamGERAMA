#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# 1. Wipe the materials that are causing the link errors
python manage.py shell -c "from academy.models import Material; Material.objects.all().delete()"

# 2. FAKE the first two migrations because the tables already exist physically
python manage.py migrate academy 0001 --fake
python manage.py migrate academy 0002 --fake

# 3. Now run the new migrations (0003 and 0004) for real
# This creates the Course table and adds the course_id column
python manage.py migrate academy

# 4. Standard completion
python manage.py migrate
python manage.py collectstatic --no-input