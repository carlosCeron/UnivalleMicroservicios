FROM python:3-alpine

MAINTAINER Carlos ceron

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN apk add --update \
     bash \
     curl \
     gcc \
     python3-dev \
     musl-dev \
     postgresql-dev \
     nodejs \
     npm \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./ /app

CMD ["python", "/app/app.py"]