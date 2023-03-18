from typing import Union

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    """
    firstname = Column(String, unique=False, index=False)
    lastname = Column(String, unique=False, index=False)
    birthday = Column(Date, unique=False, index=False)
    male_sign = Column(Boolean, unique=False, index=False)
    interests = Column(String, unique=False, index=True)
    city = Column(String, unique=False, index=True)
    """


class UserCreate(UserBase):
    password: str
    firstname: str
    lastname: str
    birthday: str #?
    male_sign: bool
    interests: str
    city: str


class User(UserBase):
    id: int
    is_active: bool

    firstname: str
    lastname: str
    birthday: str  # ?
    male_sign: bool
    interests: str
    city: str

    class Config:
        orm_mode = True