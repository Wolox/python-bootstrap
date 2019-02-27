"""Dockerfile configuration as fixture representation."""

dockerfile = """FROM python:3.6.3

RUN mkdir -p /app/{0}
COPY ./src /app/{0}/src
ADD ./docker/development/requirements.txt /app/{0}
WORKDIR /app/{0}
RUN pip install -r requirements.txt"""