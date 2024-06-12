from sqlalchemy import Column, Integer, String
from src.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
