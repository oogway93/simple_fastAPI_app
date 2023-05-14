from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres", echo=True)

session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close_all()