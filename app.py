import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models.beer import Beer
from models.base import Base

from sqlalchemy.orm import Session


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine(os.environ['DATABASE_URL'])
Base.prepare(engine, reflect=True)
session = Session(engine)


@app.route('/')
def beer_world():
    return "Welcome to Beer World"

@app.route('/beer/<id>')
def find_beer(id):
    beer = session.query(Beer).filter(Beer.id == id).first()
    return beer.description

if __name__ == '__main__':
    print("Using configs: {}".format(os.environ['APP_SETTINGS']))
    app.run()