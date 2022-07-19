from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_session
from repositories.user import UserRepository
from schema.user import User, UserBase, UserIn


router = APIRouter()


@router.get('/get-users', response_model=List[UserBase])
async def get_users(
        limit: int = 100,
        skip: int = 0,
        session: AsyncSession = Depends(get_session)
) -> List[UserBase]:
    return await UserRepository.get_all(session=session, limit=limit, skip=skip)


@router.get('/get-user', response_model=User)
async def get_user_by_email(
        email: str,
        session: AsyncSession = Depends(get_session)
) -> User:
    result = await UserRepository.get_user_by_email(session=session, email=email)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result


@router.post('/post-user', response_model=UserBase, status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserIn,
        session: AsyncSession = Depends(get_session)
) -> UserBase:
    if await UserRepository.get_user_by_email(session=session, email=user.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    return await UserRepository.create_user(session=session, user=user)
