#!/usr/bin/env bash
# exit on error
set -o errexit

# --- This is new and important ---
# Change to the directory that contains your manage.py file.
# If your project is in a subfolder named 'PersonaAI', use that.
# If not, remove or change this line.
# cd PersonaAI 

# Install all the packages from requirements.txt
pip install -r requirements.txt

# Collect all static files (CSS, JS, etc.) into one folder
python manage.py collectstatic --no-input

# Apply any database migrations. This will create your tables.
python manage.py migrate
