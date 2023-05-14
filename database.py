from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./sql_app.db")

session = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()  # I used declarative method but you can another one.


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close_all
