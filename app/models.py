from datetime import datetime
from sqlmodel import Column, Enum, Field, SQLModel
import enum

# User model

class UserBase(SQLModel):
    username: str = Field(unique=True, max_length=64)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_active: bool = Field(default=True)
    subscription_active: bool = Field(default=True)
    number_of_messages: int = Field(default=0)
    hashed_password: str = Field(default="", max_length=255)


class UserPublic(SQLModel):
    username: str
    id: int
    subscription_active: bool
    number_of_messages: int
    is_active: bool


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    username: str | None = None
    is_active: bool | None = None