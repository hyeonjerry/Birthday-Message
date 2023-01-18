from sqlalchemy.orm import Session
from passlib.context import CryptContext

from domain.user.user_schema import UserCreate
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_create: UserCreate):
    user = User(username=user_create.username,
                password=pwd_context.hash(user_create.password1))
    db.add(user)
    db.commit()


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(User.username == user_create.username).first()


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()