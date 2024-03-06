FROM python:3.12-alpine

RUN apk add --no-cache --update unixodbc-dev \
    gcc \
    unixodbc \
    musl-dev \
    libffi-dev \
    g++ \
    build-base \
    mariadb-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    libpq-dev

RUN pip install --upgrade pip
RUN pip install psycopg2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./bin/entry-point.sh /
WORKDIR /etc/pgob/code


ENTRYPOINT ["/bin/sh", "/entry-point.sh"]
