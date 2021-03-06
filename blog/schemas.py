from pydantic import BaseModel
from typing import List

from blog.database import Base


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class Show_User(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class Show_Blog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str 