from typing import List

import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship

from src.apps import Base


class SensorReading(Base):
    __tablename__ = "sensor_reading"

    id = Column(Integer, primary_key=True)
    value = Column(JSONB)

    sensor_id = Column(Integer, ForeignKey("sensor.id"))
    sensor = relationship("Sensor", back_populates="readings")


class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sensor_type = Column(String)

    fleetship_id = Column(Integer, ForeignKey("fleetship.id"))
    fleetship = relationship("FleetShip", back_populates="sensors")

    readings = relationship("SensorReading", back_populates="sensor")


class FleetShip(Base):
    __tablename__ = "fleetship"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    plant_id = Column(Integer, ForeignKey("plant.id"))
    plant = relationship("Plant", back_populates="fleetships")

    sensors = relationship("Sensor", back_populates="fleetship")


class Plant(Base):
    __tablename__ = "plant"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species_name = Column(String)
    description = Column(String)
    image = Column(String)

    fleetships = relationship("FleetShip", back_populates="plant")
