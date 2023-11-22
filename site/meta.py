import os

from flask import Flask

from local_settings import FLASK_SECRET_KEY


LANGUAGE = "en" # os.environ["LOCALE_LANGUAGE_NAME"]
APP_URL = "http://practical-cm.com"
DB_NAME = "practicalcm"

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = FLASK_SECRET_KEY