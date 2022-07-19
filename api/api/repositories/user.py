from unittest import result
from sqlalchemy import select
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from repositories.base import BaseRepository
from db.models import Users
from schema.user import User, UserIn


class UserRepository(BaseRepository):
    @classmethod
    async def get_all(cls, session: AsyncSession, limit: int = 100, skip: int = 0) -> List[User]:
        q = select(Users).limit(limit).offset(skip)
        result = [User.from_orm(item) for item in (await session.scalars(q)).all()]
        return result

    @classmethod
    async def get_user_by_email(cls, session: AsyncSession, email: str) -> User:
        q = select(Users).where(Users.email == email)
        result = await session.scalars(q)
        return result.one_or_none()
    
    @classmethod
    async def create_user(cls, session: AsyncSession, user: UserIn) -> User:    
        us = User.from_orm(user)      
        u = Users(**us.dict())
        session.add(u)
        await session.commit()
