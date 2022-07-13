from db.database import AsyncSession


class BaseRepository:
    def __init__(self, session=AsyncSession):
        self.Session = session