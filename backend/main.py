from fastapi import FastAPI

from domain.birthday import birthday_router

app = FastAPI()

app.include_router(birthday_router.router)


@app.get('/')
def index():
    return "Hello, World!"
