import datetime

from pydantic import BaseModel, validator


class MessageCreate(BaseModel):
    name: str
    message: str

    @validator('name', 'message')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Message(BaseModel):
    id: int
    name: str
    message: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True
