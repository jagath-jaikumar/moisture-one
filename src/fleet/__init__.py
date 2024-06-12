from fastapi import APIRouter
from fastcrud import crud_router

from src.db import get_session
from src.fleet import models, schemas

router = APIRouter()

plant_router = crud_router(
    session=get_session,
    model=models.Plant,
    create_schema=schemas.PlantCreateSchema,
    update_schema=schemas.PlantUpdateSchema,
    path="/plant",
    tags=["Plant"],
)

sensor_router = crud_router(
    session=get_session,
    model=models.Sensor,
    create_schema=schemas.SensorCreateSchema,
    update_schema=schemas.SensorUpdateSchema,
    path="/sensor",
    tags=["Sensor"],
)

fleetship_router = crud_router(
    session=get_session,
    model=models.FleetShip,
    create_schema=schemas.FleetShipCreateSchema,
    update_schema=schemas.FleetShipUpdateSchema,
    path="/fleet-ship",
    tags=["FleetShip"],
)


sensor_reading_router = crud_router(
    session=get_session,
    model=models.SensorReading,
    create_schema=schemas.SensorReadingCreateSchema,
    update_schema=schemas.SensorReadingUpdateSchema,
    path="/sensor-reading",
    tags=["SensorReading"],
    deleted_methods=["delete"],
)

router.include_router(plant_router)
router.include_router(sensor_router)
router.include_router(fleetship_router)
router.include_router(sensor_reading_router)
