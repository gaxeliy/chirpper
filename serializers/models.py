import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    login: str
    name: str


class ChirpPydanticModel(BaseModel):
    author: User
    text: str
    replies: Optional[List['ChirpPydanticModel']]
    publish_date: datetime.datetime
