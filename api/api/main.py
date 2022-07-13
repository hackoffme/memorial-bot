import asyncio
from fastapi import FastAPI
import uvicorn
from database.database import init_models
from database.models import User, Post


app = FastAPI(title='API memorial bot')


def db():
    asyncio.run(init_models())


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
    # db()
