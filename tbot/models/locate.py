from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

from tbot.models.database import Base


class PlayerScore(Base):
    __tablename__ = "playerscore"

    user_id = Column(BigInteger, primary_key=True,
                     unique=True, autoincrement=False)
    score = Column(Integer, default=0)

# class Locate(Base):

#     __tablename__ = 'location'
#     __tableargs__ = {
#         'comment': 'Контент, привязанный к локации'
#     }

#     location_id = Column(
#         Integer,
#         nullable=False,
#         unique=True,
#         primary_key=True,
#         autoincrement=True
#     )
#     name = Column(String(128), comment='Наименование темы')
#     location = Column(Geometry('POINT'))
#     description = Column(Text, comment='Описание темы')

#     def __repr__(self):
#         return f'{self.topic_id} {self.name} {self.description}'
