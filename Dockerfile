# Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Prevent Python from writing .pyc files & enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 5. Copy project files
COPY . /app/

# 6. Expose backend port
EXPOSE 8000