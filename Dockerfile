FROM python:3.9-alpine as build

WORKDIR /usr/src/api

COPY pyproject.toml poetry.lock ./

RUN apk --no-cache add poetry \
    && \
    poetry export --without-hashes -f requirements.txt > requirements.txt

# ====================
FROM python:3.9-alpine

WORKDIR /usr/src/api

COPY --from=build /usr/src/api/requirements.txt ./

RUN adduser -S api \
    && \
    apk --no-cache add build-base \
    && \
    pip3 install --no-cache-dir -r requirements.txt

USER api
