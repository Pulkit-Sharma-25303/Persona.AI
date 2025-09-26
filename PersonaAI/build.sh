#!/usr/bin/env bash
# exit on error
set -o errexit

# Install all the packages from requirements.txt
pip install -r requirements.txt

# Collect all static files (CSS, JS, etc.) into one folder
python manage.py collectstatic --no-input

# Apply any database migrations. This will create your tables.
python manage.py migrate
