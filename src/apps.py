from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
import datetime


class Base(DeclarativeBase):
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


from src.admin import models as admin_models
from src.fleet import models as fleet_models
