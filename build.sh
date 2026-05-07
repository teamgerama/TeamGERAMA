#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt


# ... existing build steps (pip install, etc.) ...

# 1. Clean up bad data
python manage.py shell -c "from academy.models import Material; Material.objects.all().delete()"

# 2. Tell Django the first two migrations (School/Dept/Prog) are already done
python manage.py migrate academy 0002 --fake

# 3. Run the new migrations (Course creation and Material update) for real
python manage.py migrate academy

# 4. Final sync for everything else
python manage.py migrate
python manage.py collectstatic --no-input