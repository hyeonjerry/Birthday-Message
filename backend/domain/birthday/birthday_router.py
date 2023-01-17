from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Birthday
from domain.birthday import birthday_schema, birthday_crud

router = APIRouter(prefix="/api/birthday")


@router.get("/detail/{birthday_id}", response_model=birthday_schema.Birthday)
def birthday_detail(birthday_id: str, db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, birthday_id)
    return birthday
