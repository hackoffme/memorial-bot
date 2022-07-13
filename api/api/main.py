import asyncio
from fastapi import FastAPI
import uvicorn
from db.database import init_models
from db.models import User, Post

from db.database import AsyncSession
from repositories.user import UserRepository


app = FastAPI(title='API memorial bot')


def db():
    asyncio.run(init_models())


if __name__ == "__main__":
    # uvicorn.run('main:app', reload=True)
    # db()
    u = UserRepository()
    # print(dir(u))

    asyncio.run(u.get_all())

