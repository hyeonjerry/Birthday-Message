from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from models import Birthday
from domain.birthday import birthday_schema, birthday_crud

router = APIRouter(prefix="/api/birthday")


@router.get("/detail/{birthday_id}", response_model=birthday_schema.Birthday)
def birthday_detail(birthday_id: str, db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, birthday_id)
    return birthday


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def birthday_create(_birthday_create: birthday_schema.BirthdayCreate,
                    db: Session = Depends(get_db)):
    birthday_crud.create_birthday(db, _birthday_create)
