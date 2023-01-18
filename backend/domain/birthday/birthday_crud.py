import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models import Birthday
from domain.birthday.birthday_schema import BirthdayCreate, BirthdayUpdate, BirthdayDelete


def get_birthday(db: Session, birthday_id: str):
    birthday = db.query(Birthday).get(birthday_id)
    return birthday


def create_birthday(db: Session, birthday_create: BirthdayCreate):
    def gen_id():
        while True:
            id = uuid.uuid4().hex
            if (db.query(Birthday).get(id)):
                continue
            return id

    birthday = Birthday(id=gen_id(),
                        name=birthday_create.name,
                        bdate=birthday_create.bdate,
                        introduce=birthday_create.introduce,
                        created_at=datetime.now())
    db.add(birthday)
    db.commit()


def update_birthday(db: Session, birthday: Birthday, birthday_update: BirthdayUpdate):
    birthday.name = birthday_update.name
    birthday.bdate = birthday_update.bdate
    birthday.introduce = birthday_update.introduce
    db.add(birthday)
    db.commit()


def delete_birthday(db: Session, birthday: Birthday):
    db.delete(birthday)
    db.commit()
