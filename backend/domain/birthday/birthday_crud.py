import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models import Birthday, User
from domain.birthday.birthday_schema import BirthdayCreate, BirthdayUpdate


def get_birthday(db: Session, birthday_id: str):
    birthday = db.query(Birthday).get(birthday_id)
    birthday.messages.reverse()
    return birthday


def get_birthday_list(db: Session, user: User):
    birthday_list = db.query(Birthday).filter(Birthday.user_id == user.id)
    total = birthday_list.distinct().count()
    birthday_list = birthday_list.order_by(
        Birthday.created_at.desc()).distinct().all()
    return total, birthday_list


def create_birthday(db: Session, birthday_create: BirthdayCreate, user: User):
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
                        created_at=datetime.now(),
                        user=user)
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
