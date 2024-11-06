FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/appointment_app

COPY requirements.txt .
COPY .env.example .env

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
