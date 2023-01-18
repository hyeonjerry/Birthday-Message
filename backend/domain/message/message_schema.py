import datetime

from pydantic import BaseModel, validator


class MessageCreate(BaseModel):
    message: str

    @validator('message')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
