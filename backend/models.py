from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, Date
from sqlalchemy.orm import relationship

from database import Base


class Birthday(Base):
    __tablename__ = "birthday"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    bdate = Column(Date, nullable=False)
    introduce = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="birthdays")


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    birthday_id = Column(String, ForeignKey("birthday.id"))
    birthday = relationship("Birthday", backref="messages")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
