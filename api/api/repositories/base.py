from typing_extensions import Self
from db.database import AsyncSession


class BaseRepository:
    ...
    # def __new__(cls: type[Self]) -> Self:
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(BaseRepository, cls).__new__(cls)
    #     return cls.instance