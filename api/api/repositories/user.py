from sqlalchemy import select
from typing import List

from repositories.base import BaseRepository
from db.models import Users
from schema.user import User, UserIn


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        q = select(Users).limit(limit).offset(skip)
        async with self.Session() as session:
            result =[User.from_orm(item) for item in (await session.scalars(q)).all()]
            return result
    