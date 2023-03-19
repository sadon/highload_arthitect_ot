import datetime
from typing import Union

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    first_name: str
    second_name: str
    birthday: datetime.date #?
    male_sign: bool
    biography: str
    city: str


class User(UserBase):
    id: int
    is_active: bool

    first_name: str
    second_name: str
    birthday: datetime.date  # ?
    male_sign: bool
    biography: str
    city: str

    class Config:
        orm_mode = True