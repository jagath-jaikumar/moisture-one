from pydantic import BaseModel


class PlantCreateSchema(BaseModel):
    name: str
    species_name: str
    description: str
    image: str


class PlantUpdateSchema(BaseModel):
    name: str
    species_name: str
    description: str
    image: str


class SensorCreateSchema(BaseModel):
    name: str


class SensorUpdateSchema(BaseModel):
    name: str


class MonitorCreateSchema(BaseModel):
    name: str
    sensor_id: int


class MonitorUpdateSchema(BaseModel):
    name: str
    sensor_id: int


class SensorReadingCreateSchema(BaseModel):
    monitor_id: int
    value: dict


class SensorReadingUpdateSchema(BaseModel):
    monitor_id: int
    value: dict
