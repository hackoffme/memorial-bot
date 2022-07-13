
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from database.database import Base

class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(DECIMAL(9,6))
    lon = Column(DECIMAL(9,6))
    title = Column(String)
    text = Column(String)
    is_active = Column(Boolean, default=True)