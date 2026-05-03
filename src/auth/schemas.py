from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import Optional

class UserCreateModel(BaseModel):
    username: str = Field(max_length=30)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)
    firstname: str = Field(max_length=20)
    lastname: str = Field(max_length=20)

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    firstname: str
    lastname: str
    is_verified: bool
    password_hash: str
    created_at: datetime
    updated_at: datetime

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)