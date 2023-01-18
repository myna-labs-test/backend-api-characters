FROM python:3.10-alpine
WORKDIR /character
RUN apk add --no-cache make
RUN apk add --no-cache poetry
#RUN apk --update add py-pip openssl ca-certificates py-openssl wget python-devel
#RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev  py-pip build-base
COPY poetry.lock pyproject.toml ./
RUN poetry install || true
COPY ./api ./api
COPY ./migrations ./migrations
COPY ./.env ./.env
COPY ./Makefile ./Makefile
CMD make run