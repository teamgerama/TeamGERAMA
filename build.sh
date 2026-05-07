#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt


# ... existing build steps (pip install, etc.) ...

# 1. Wipe out any bad data first
python manage.py shell -c "from academy.models import Material; Material.objects.all().delete()"

# 2. Force Django to 'forget' the messy migrations 0003 and 0004
python manage.py migrate academy zero --fake

# 3. Now run them for real so the 'course_id' column is actually created
python manage.py migrate academy

# 4. Finish the rest
python manage.py migrate
python manage.py collectstatic --no-input