import datetime

from pydantic import BaseModel, validator


class Birthday(BaseModel):
    id: str
    name: str
    bdate: datetime.date
    introduce: str

    class Config:
        orm_mode = True


class BirthdayCreate(BaseModel):
    name: str
    bdate: datetime.date
    introduce: str

    @validator('name', 'bdate', 'introduce')
    def not_empty(cls, v):
        if not v or type(v) == str and not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
