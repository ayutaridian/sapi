import os
import sqlite3
from flask import Flask, session, request, redirect, render_template
import logging
import requests
import helpers
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from helpers import login_required

app = Flask(__name__)

app.run(debug=True)

# Config a session
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#app.config["SECRET_KEY"] = "abcdef"

# Logging
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')

import sqlite3
conn = sqlite3.connect("db2.sqlite3", check_same_thread=False)
c = conn.cursor()


# sapi
@app.route("/")
def signin():
    return render_template("sapi.html")