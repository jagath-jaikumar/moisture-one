from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.apps import Base


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
