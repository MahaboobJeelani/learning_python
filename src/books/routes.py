from src.books.books_data import books
from fastapi import FastAPI, status, HTTPException, APIRouter
from src.books.schames import Book, UpdateBook
from typing import List, Optional

book_router = APIRouter()


@book_router.get("/")
def health_check():
    return {"message": "Server is health is good"}

@book_router.get('/greed ')
def greed_name(name:Optional[str] = "User"):
    return {"message":f"{name}"}


@book_router.get("/", response_model=List[Book])
async def get_books():
    return await books


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(book_data:Book) -> dict:
     new_book = book_data.model_dump()
     books.append(new_book)
     return new_book


@book_router.get('/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
          if book["id"] == book_id:
               return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.patch("/{book_id}")
async def update_book(book_id:int, update_book: UpdateBook) -> dict:
    for book in books:
        if book["id"] == book_id:
               book["title"] = update_book.title
               book["author"] = update_book.author
               book["publisher"] = update_book.publisher
               book["page_count"] = update_book.page_count
               book["language"] = update_book.language
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

@book_router.delete("/{book_id}")
async def delete_book(book_id:int) -> dict:
    for book in books:
         if book['id'] == book_id:
              books.remove(book)
              return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book deleted")    