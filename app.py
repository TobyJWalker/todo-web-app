import os, peewee, re
from hashlib import sha256
from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from lib.models import *

# create a Flask app instance and set secret key
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

# create index route
@app.route("/", methods=["GET"])
def index():
    return 'Hello, World!'

# start the server
if __name__ == "__main__":
    if os.environ.get("APP_ENV") == "dev":
        app.run(
            debug=True, 
            host='0.0.0.0', 
            port=5001, 
            ssl_context=('todo-cert.pem', 'todo-cert-key.pem')
            )
    else:
        app.run(
            debug=False, 
            host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000)),
            ssl_context=('todo-cert.pem', 'todo-cert-key.pem')
            )