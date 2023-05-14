from sqlalchemy import Column, String, Integer
from database import Base


class Book(Base):
    """Book model"""
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    author = Column(String, unique=True, index=True)
