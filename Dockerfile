# Use Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
