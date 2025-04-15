FROM python:3.11-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# non-root user
RUN useradd -m django

# working directory and  requirements
WORKDIR /app
COPY requirements.txt .

#  Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# the rest of the application files
COPY . .

#  ownership of app files to django user
RUN chown -R django:django /app

# Switch to non-root user
USER django

# Run Gunicorn as the entry point
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecommerce.wsgi"]
