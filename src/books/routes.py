
from typing import Optional, List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel, BookDataModel
from fastapi import APIRouter, status, Header, HTTPException

book_routes = APIRouter()



@book_routes.get('/', response_model = List[Book])
async def get_books():
    return books

@book_routes.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book:Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@book_routes.get('/{book_id}')
async def create_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_routes.patch('/{book_id}')
async def create_book(book_id:int, book_update_model:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_model.title
            book['author'] = book_update_model.author
            book['publisher'] = book_update_model.publisher
            book['page_count'] = book_update_model.page_count
            book['language'] = book_update_model.language
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_routes.delete('/{book_id}')
async def create_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# @book_routes.get("/")
# async def read_root():
#     return {"message": "Hello World"}

# @book_routes.get('/greet/{name}')
# async def greet_name(name:str) -> dict:
#     return {"message":f'Hello {name}'}

# using query parameter and path parameter
@book_routes.get('/greet')
async def greet_query(name:Optional[str] = "User", age:int = 0) -> dict:
    return {"message":f'Hello {name} and your age is {age}'}



@book_routes.post('/create')
async def create_book(book_data:BookDataModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@book_routes.get('/get_headers',  status_code = 201)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
    ):
    request_headers = {} 
    request_headers["Accept"] = accept
    request_headers["Content_Type"] = content_type
    request_headers["User_Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
