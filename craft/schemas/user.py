from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str = Field(unique=True)
    password: str = Field(min_length=8)
    dob: datetime.date | None = None


class DbUser(User, Document):
    hashed_password: str
    disabled: bool = False
