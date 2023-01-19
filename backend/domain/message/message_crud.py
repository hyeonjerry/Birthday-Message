from datetime import datetime

from sqlalchemy.orm import Session

from models import Birthday, Message
from domain.message.message_schema import MessageCreate


def create_message(db: Session, birthday: Birthday, message_create: MessageCreate, ip_addr: str):
    message = Message(name=message_create.name,
                      message=message_create.message,
                      birthday=birthday,
                      ip_addr=ip_addr,
                      created_at=datetime.now())
    db.add(message)
    db.commit()
