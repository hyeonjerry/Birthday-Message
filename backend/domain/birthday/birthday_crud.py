from sqlalchemy.orm import Session

from models import Birthday


def get_birthday(db: Session, birthday_id: str):
    birthday = db.query(Birthday).get(birthday_id)
    return birthday
