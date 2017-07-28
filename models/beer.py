from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Beer(Base):
    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    # brewer_id=
    name = db.Column(db.String())
    # category_id=
    # styled_id=
    abv = db.Column(db.Float)
    description = db.Column(db.String())
    last_updated = db.Column(db.DateTime())

    def __init__(self, name, abv, description, last_updated):
        self.name = name
        self.abv = abv
        self.description = description
        self.last_updated = last_updated

    def __repr__(self):
        return '<id {}>'.format(self.id)
