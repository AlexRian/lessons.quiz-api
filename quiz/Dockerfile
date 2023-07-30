FROM python:3.8.3-alpine

RUN apk add postgresql-dev jpeg-dev zlib-dev gcc python3-dev musl-dev make libffi-dev

WORKDIR /usr/src/quiz

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install uvicorn

COPY . .
