from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.birthday import birthday_schema, birthday_crud
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/birthday",
    tags=['birthday'],
)


@router.get("/list", response_model=birthday_schema.BirthdayList)
def birthday_list(db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    total, _birthday_list = birthday_crud.get_birthday_list(db, current_user)
    return {
        'total': total,
        'birthday_list': _birthday_list,
    }


@router.get("/detail/{birthday_id}", response_model=birthday_schema.Birthday)
def birthday_detail(birthday_id: str, db: Session = Depends(get_db)):
    birthday = birthday_crud.get_birthday(db, birthday_id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    return birthday


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def birthday_create(_birthday_create: birthday_schema.BirthdayCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    birthday_crud.create_birthday(db, _birthday_create, current_user)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def birthday_update(_birthday_update: birthday_schema.BirthdayUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    birthday = birthday_crud.get_birthday(db, _birthday_update.id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != birthday.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    birthday_crud.update_birthday(db, birthday, _birthday_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def birthday_delete(_birthday_delete: birthday_schema.BirthdayDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    birthday = birthday_crud.get_birthday(db, _birthday_delete.id)
    if not birthday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="테이터를 찾을 수 없습니다.")
    if current_user.id != birthday.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    birthday_crud.delete_birthday(db, birthday)
