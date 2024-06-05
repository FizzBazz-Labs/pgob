FROM python:3.12-bullseye


RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  wkhtmltopdf \
  libmemcached-dev \
  build-essential \
  libsqlite3-mod-spatialite binutils libproj-dev gdal-bin libgdal28 libgeoip1 \
  default-libmysqlclient-dev default-mysql-client \
  libpq-dev \
  unzip libaio1 \
  libenchant-2-2 \
  gettext \
  wget \
  git \
  pkg-config \
  locales \
  locales-all \
  libreoffice-writer \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install psycopg2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LC_TIME=es_ES.UTF-8

COPY ./bin/entry-point.sh /
WORKDIR /etc/pgob/code


ENTRYPOINT ["/bin/sh", "/entry-point.sh"]
