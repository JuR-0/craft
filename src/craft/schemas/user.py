from beanie import Document
from pydantic import BaseModel, Field
import datetime
from beanie import before_event, Insert
from craft.auth.password import hash_password


class User(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str = Field(unique=True)
    password: str = Field(min_length=8)
    dob: datetime.date | None = None

    @before_event(Insert)
    def capitalize_name(self):
        self.password = hash_password(self.password)


class DbUser(User, Document):
    disabled: bool = False
