from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from models.base import Base

class Beer(Base):
    __tablename__ = 'beers'

    id = Column(Integer, primary_key=True)
    # brewer_id=
    name = Column(String())
    # category_id=
    # styled_id=
    abv = Column(Float)
    description = Column(String())
    last_updated = Column(DateTime())

    def __init__(self, name, abv, description, last_updated):
        self.name = name
        self.abv = abv
        self.description = description
        self.last_updated = last_updated

    def __repr__(self):
        return '<id {}>'.format(self.id)
