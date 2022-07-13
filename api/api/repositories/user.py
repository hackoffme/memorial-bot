from sqlalchemy import select
from typing import List

from repositories.base import BaseRepository
from db.models import User


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0):  #: ->List[User]
        statement = select(User)
        async with self.Session() as session:
            # await session.execute(statement)
            return session.query(User).all()
