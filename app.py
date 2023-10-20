import os, peewee, re
from hashlib import sha256
from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from seeds.seed_db import *

# call to create tables in case they haven't already been created
create_db_tables()

# create a Flask app instance
app = Flask(__name__)

# set the secret key for the session
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

# create index route
@app.route("/", methods=["GET"])
def index():
    return 'Hello, World!'

# start the server
if __name__ == "__main__":
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=5001, 
        ssl_context=('todo-cert.pem', 'todo-cert-key.pem')
        )