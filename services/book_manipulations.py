from models.book import Book
from sqlalchemy.orm import Session
from dto import book


def get_book(id: int, db):  # get function, which take a book and display data in a 'docs'.
    return db.query(Book).filter(id == Book.id).first()


def create_book(data: book.Book, db: Session):  # create a book: you should enter only title and author of book.
    book = Book(title=data.title, author=data.author)
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
    except Exception as exc:
        print(exc)

    return book


def update_book(id: int, data: book.Book,
                db: Session):  # update function, which take a book by an ID and change data about it.
    book = db.query(Book).filter(id == Book.id).first()

    book.title = data.title
    book.author = data.author

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def remove_book(id: int, db: Session):  # remove function, which remove book by an ID.
    book = db.query(Book).filter(id == Book.id).delete()
    db.commit()

    return book
