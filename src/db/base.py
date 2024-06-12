from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from src.admin import models as admin_models
from src.fleet import models as fleet_models
