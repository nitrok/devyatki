FROM python:3.10-slim

LABEL maintainer="alex@orlov.team"

ENV STATIC_ROOT /var/lib/django-static
ENV DATABASE_URL sqlite:////var/lib/django-db/devyatki.sqlite

RUN mkdir /var/lib/django-db
VOLUME /var/lib/django-db

EXPOSE 8000

RUN apt-get update &&  \
    apt-get --no-install-recommends install -y build-essential locales-all gettext &&  \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pipenv==2022.4.21 pip uwsgi==2.0.20

COPY Pipfile Pipfile.lock /
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /src
COPY src /src

ENV NO_CACHE=On
RUN ./manage.py compilemessages
RUN ./manage.py collectstatic --noinput
ENV NO_CACHE=Off


CMD ./manage.py migrate && uwsgi --master --http :8000 --module app.wsgi --workers 2 --threads 2 --harakiri 25 --max-requests 1000 --log-x-forwarded-for