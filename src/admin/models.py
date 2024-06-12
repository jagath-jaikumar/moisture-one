from sqlalchemy import Column, Integer, String, Boolean
from src.apps import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class APIKey(Base):
    __tablename__ = "api_key"

    id = Column(Integer, primary_key=True)
    key = Column(String)
    enabled = Column(Boolean, default=True)
