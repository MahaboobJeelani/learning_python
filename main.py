from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


books = [
    {
        "id": 1,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
    {
        "id": 7,
        "title": "Think python",
        "author": "Allen b.Downey",
        "publisher": "O Relly Media",
        "published_date": "2021-01-02",
        "page_count": 18,
        "language": "English",
    },
]


@app.get("/books")
async def get_all_books():
    return books


@app.get("/{id}")
async def get_single_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books")
async def create_book(book_data: Book):
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.get("/")
async def fun():
    return {"message": "Hello World"}


@app.get("/headers")
async def headers(accept: str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    return request_headers
