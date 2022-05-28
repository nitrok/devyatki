FROM python:3.10-alpine

LABEL maintainer="alex@orlov.team"

ENV DATABASE_URL sqlite:////var/lib/django-db/devyatki.sqlite
ENV PROJECT_DIR /usr/local/src
ENV PROJECT_DATA_DIR /var/lib/django-db

RUN mkdir ${PROJECT_DATA_DIR}


WORKDIR ${PROJECT_DIR}
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/


RUN apk add --no-cache make && \
    pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear && \
    pip uninstall pipenv -y

COPY src ./
COPY Makefile ./
