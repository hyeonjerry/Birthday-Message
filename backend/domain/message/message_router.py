from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.message import message_schema, message_crud
from domain.birthday import birthday_crud

router = APIRouter(
    prefix="/api/message",
    tags=["message"],
)


@router.post("/create/{birthday_id}", status_code=status.HTTP_204_NO_CONTENT)
def message_create(birthday_id: str,
                   _message_create: message_schema.MessageCreate,
                   request: Request,
                   db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, birthday_id)
    ip_addr = request.client.host
    if not birthday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    message_crud.create_message(db, birthday, _message_create, ip_addr)
