FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
COPY .env.example .env

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
