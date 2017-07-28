import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Set up the Flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print("Using configs: {}".format(os.environ['APP_SETTINGS']))

# Set up everything related to db
db = SQLAlchemy(app)

# need to set up the app before you can import controllers since controllers depends on app
from beer import controllers