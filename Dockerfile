# Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Make entrypoint executable inside the container
RUN ["chmod", "+x", "/app/entrypoint.sh"]

RUN ["python manage.py import_books"]

# Use the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command to run Django
CMD ["gunicorn", "rumipress.wsgi:application", "--bind", "0.0.0.0:8000"]
