from fastapi import APIRouter
from typing import List

from repositories.user import UserRepository
from schema.user import User


router = APIRouter()


@router.get('/', response_model=List[User])
async def read_user(
        limit: int = 100,
        skip: int = 0
):
    return await UserRepository().get_all(limit=limit, skip=skip)
