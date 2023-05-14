from pydantic import BaseModel


class Book(BaseModel):
    """Pydantic model of book"""
    title: str
    author: str
