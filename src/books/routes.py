from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from src.books.schames import BookModel, UpdateBook, BookCreateModel
from src.books.service import BookService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model=List[BookModel])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookModel)
async def create_a_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return new_book

@book_router.get("/{book_uid}", response_model=BookModel)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_uid, session)
    if book: 
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/{book_uid}", response_model=BookModel)
async def update_book(book_uid: str, update_book: UpdateBook, session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.updated_book(book_uid, update_book, session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    deleted = await book_service.delete_book(book_uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None