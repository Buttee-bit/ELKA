FROM python:3.11-slim-buster as backend

RUN apt-get update \
    && apt-get -y install libpq-dev gcc libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
    
COPY ../backend/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt


COPY ../backend /app/backend
WORKDIR /app/backend
