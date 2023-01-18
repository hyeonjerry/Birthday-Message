from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.birthday import birthday_schema, birthday_crud

router = APIRouter(
    prefix="/api/birthday",
    tags=['birthday'],
)


@router.get("/detail/{birthday_id}", response_model=birthday_schema.Birthday)
def birthday_detail(birthday_id: str, db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, birthday_id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    return birthday


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def birthday_create(_birthday_create: birthday_schema.BirthdayCreate,
                    db: Session = Depends(get_db)):
    birthday_crud.create_birthday(db, _birthday_create)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def birthday_update(_birthday_update: birthday_schema.BirthdayUpdate,
                    db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, _birthday_update.id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    birthday_crud.update_birthday(db, birthday, _birthday_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def birthday_delete(_birthday_delete: birthday_schema.BirthdayDelete,
                    db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, _birthday_delete.id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="테이터를 찾을 수 없습니다.")
    birthday_crud.delete_birthday(db, birthday)
