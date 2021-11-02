from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///app.db', echo=True)


Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


###function name: db_query()
###usage: added to facilitate DB table querying
def db_query():
    db_session = scoped_session(sessionmaker(bind=engine))
    Base.query = db_session.query_property()