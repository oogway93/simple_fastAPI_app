from sqlalchemy import Boolean, Column, String, Integer
from database import Base


class Book(Base):
    __tablename__ = 'Books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)