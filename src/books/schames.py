from pydantic import BaseModel
import uuid
from datetime import datetime

class Book(BaseModel):
        uid: uuid.UUID
        title: str
        author: str 
        publisher: str
        published_date: str
        page_count: str
        language: str
        created_at: datetime
        update_at: datetime

class BookCreateModel(BaseModel):
        title: str
        author: str 
        publisher: str
        published_date: str
        page_count: str
        language: str

class UpdateBook(BaseModel):
        title: str
        author: str 
        publisher: str
        page_count: str
        language: str