from fastapi import FastAPI
from src.books.routes import book_routes

version = "v1"
app = FastAPI(
    title="Books", description="Learning How fastapi will work", version=version
)

app.include_router(book_routes, prefix=f"/api/{version}/books")
