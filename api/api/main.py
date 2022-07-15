import asyncio
from fastapi import FastAPI
import uvicorn
from db.database import init_models
from db.models import Users, Posts

from db.database import AsyncSession
from repositories.user import UserRepository


app = FastAPI(title='API memorial bot')


def db():
    asyncio.run(init_models())


if __name__ == "__main__":
    # uvicorn.run('main:app', reload=True)
    # db()
    u = UserRepository()

    loop = asyncio.get_event_loop()
    getall = loop.run_until_complete(u.get_all())
    

