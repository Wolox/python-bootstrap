"""__init__.py service as fixture representation."""

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