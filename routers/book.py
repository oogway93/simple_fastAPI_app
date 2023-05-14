from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import book_manipulations as BookService
from dto import book as BookDTO

router = APIRouter()


@router.post('/', tags=["book"])
async def post(data: BookDTO.Book = None, db: Session = Depends(get_db)):
    return BookService.create_book(data, db)


@router.get('/{id}', tags=["book"])
async def get(id: str = None, db: Session = Depends(get_db)):
    return BookService.get_book(id, db)


@router.put('/{id}', tags=["book"])
async def put(id: int, data: BookDTO.Book = None, db: Session = Depends(get_db)):
    return BookService.update_book(id, data, db)


@router.delete('/{id}', tags=["book"])
async def delete(id: int, db: Session = Depends(get_db)):
    return BookService.remove_book(id, db)
