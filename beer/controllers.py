import os
from beer import app
from beer.models.beer import Beer
from beer.models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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