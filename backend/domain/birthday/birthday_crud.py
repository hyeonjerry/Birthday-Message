import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models import Birthday
from domain.birthday.birthday_schema import BirthdayCreate


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
