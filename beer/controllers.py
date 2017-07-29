import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from beer import app
from beer.models.base import Base
from beer.models.beer import Beer

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

@app.route('/beer/<id>/recommendation')
def get_beer_recommendation(id):
    beer = session.query(Beer).filter(Beer.id == id).first()
    return beer.id