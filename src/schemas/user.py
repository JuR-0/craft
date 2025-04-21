from beanie import Document
from pydantic import Field


class User(Document):
    first_name: str
    last_name: str
    email: str = Field(unique=True)
    password: str = Field(min_length=8)
