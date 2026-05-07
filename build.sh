#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt


# ... existing build steps (pip install, etc.) ...

# TEMPORARY: Clear the bad data and force the migration
python manage.py shell -c "from academy.models import Material; Material.objects.all().delete()"
python manage.py migrate academy 0003 --fake
python manage.py migrate
python manage.py collectstatic --no-input