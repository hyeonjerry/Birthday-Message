from fastapi import FastAPI

from domain.birthday import birthday_router
from domain.message import message_router
from domain.user import user_router

app = FastAPI()

app.include_router(birthday_router.router)
app.include_router(message_router.router)
app.include_router(user_router.router)


@app.get('/')
def index():
    return "Hello, World!"
