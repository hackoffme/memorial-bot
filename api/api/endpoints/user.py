from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_user(
    limit: int = 100,
    skip: int = 0
):
    return