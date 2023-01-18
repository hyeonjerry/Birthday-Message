from datetime import datetime

from sqlalchemy.orm import Session

from models import Birthday, Message
from domain.message.message_schema import MessageCreate


def create_message(db: Session, birthday: Birthday, message_create: MessageCreate):
    message = Message(name=message_create.name,
                      message=message_create.message,
                      birthday=birthday,
                      created_at=datetime.now())
    db.add(message)
    db.commit()
