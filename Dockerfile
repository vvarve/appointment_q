FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
COPY .env.sample .env

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
