from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime, date

class BookModel(BaseModel):
        uid: uuid.UUID
        title: str
        author: str 
        publisher: str
        published_date: date
        page_count: int
        language: str
        created_at: datetime
        updated_at: datetime

        # model_config = ConfigDict(from_attributes=True)
        model_config = ConfigDict(from_attributes=True)

class BookCreateModel(BaseModel):
        title: str
        author: str 
        publisher: str
        published_date: date
        page_count: int
        language: str

class UpdateBook(BaseModel):
        title: str | None = None
        author: str | None = None
        publisher: str | None = None
        page_count: int | None = None
        language: str | None = None