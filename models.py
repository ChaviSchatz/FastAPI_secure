from typing import Union, Optional, Dict
from pydantic import BaseModel, constr, EmailStr, Field
from uuid import UUID, uuid4

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: constr(min_length=3)
    email: Union[EmailStr, None] = None
    password: Union[constr(min_length=8), None] = None
    disabled: Union[bool, None] = None
    todos: Union[list, None] = []

class UserInDB(User):
    hashed_password: str


class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    owner: str
    completed: bool


