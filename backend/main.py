from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.birthday import birthday_router
from domain.message import message_router
from domain.user import user_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(birthday_router.router)
app.include_router(message_router.router)
app.include_router(user_router.router)


@app.get('/')
def index():
    return "Hello, World!"
