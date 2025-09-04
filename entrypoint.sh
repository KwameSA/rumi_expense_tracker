#!/bin/sh

# Exit immediately if a command fails
set -e

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations (optional but recommended)
echo "Applying database migrations..."
python manage.py migrate

python import_books.py

# Run the main process (Gunicorn)
exec "$@"
