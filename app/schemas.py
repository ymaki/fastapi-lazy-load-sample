from typing import List

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    name: str
    items: List[Item] = []

    class Config:
        orm_mode = True