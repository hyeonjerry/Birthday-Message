import datetime

from pydantic import BaseModel, validator

from domain.message.message_schema import Message


class Birthday(BaseModel):
    id: str
    name: str
    bdate: datetime.date
    introduce: str
    created_at: datetime.datetime
    messages: list[Message] = []

    class Config:
        orm_mode = True


class BirthdayList(BaseModel):
    total: int = 0
    birthday_list: list[Birthday] = []


class BirthdayCreate(BaseModel):
    name: str
    bdate: datetime.date
    introduce: str

    @validator('name', 'bdate', 'introduce')
    def not_empty(cls, v):
        if not v or type(v) == str and not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class BirthdayUpdate(BirthdayCreate):
    id: str


class BirthdayDelete(BaseModel):
    id: str
