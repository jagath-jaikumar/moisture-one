from fastcrud import crud_router
from src.fleet import schemas
from src.fleet import models
from src.db import get_session
from fastapi import APIRouter

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

monitor_router = crud_router(
    session=get_session,
    model=models.Monitor,
    create_schema=schemas.MonitorCreateSchema,
    update_schema=schemas.MonitorUpdateSchema,
    path="/monitor",
    tags=["Monitor"],
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
router.include_router(monitor_router)
router.include_router(sensor_reading_router)