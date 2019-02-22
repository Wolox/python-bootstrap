"""Docker-compose, Dockerfile, service __init__ and requirements 
Representation."""
service = """

  {0}:
    build: 
      context: ./{0}/
      dockerfile: ./docker/development/Dockerfile
    command: python ./src/__init__.py
    volumes:
      - .:/{0}
    env_file:
      - ./{0}/docker/development/env/public
      - ./{0}/docker/development/env/private
    ports:
      - "{1}:{1}" """

dockerfile = """FROM python:3.6.3

RUN mkdir -p /app/{0}
COPY ./src /app/{0}/src
ADD ./docker/development/requirements.txt /app/{0}
WORKDIR /app/{0}
RUN pip install -r requirements.txt"""

service_init = """from flask import Flask
import os
import socket


app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>{0}</h3>"
    return html.format()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port={1})"""

requirements = """Flask"""