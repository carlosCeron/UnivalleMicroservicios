FROM python:3-alpine

MAINTAINER Carlos Ceron

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  curl \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY . /app

CMD python app.py run -h 0.0.0.0
