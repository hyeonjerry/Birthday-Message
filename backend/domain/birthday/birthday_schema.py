import datetime

from pydantic import BaseModel, validator


class Birthday(BaseModel):
    id: str
    name: str
    bdate: datetime.date
    introduce: str

    class Config:
        orm_mode = True
