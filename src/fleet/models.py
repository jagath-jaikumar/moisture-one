from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship

from src.apps import Base


class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Monitor(Base):
    __tablename__ = "monitor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # sensor = relationship("Sensor", back_populates="monitor")


class SensorReading(Base):
    __tablename__ = "sensor_reading"

    id = Column(Integer, primary_key=True)
    value = Column(JSONB)
    # monitor = relationship("Monitor", back_populates="sensor")


class Plant(Base):
    __tablename__ = "plant"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species_name = Column(String)
    description = Column(String)
    image = Column(String)

    # monitors: Mapped[List["Monitor"]] = relationship(back_populates="plant")
