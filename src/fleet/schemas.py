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
    sensor_type: str
    fleetship_id: int


class SensorUpdateSchema(BaseModel):
    name: str
    sensor_type: str
    fleetship_id: int


class FleetShipCreateSchema(BaseModel):
    name: str
    plant_id: int


class FleetShipUpdateSchema(BaseModel):
    name: str
    plant_id: int


class SensorReadingCreateSchema(BaseModel):
    sensor_id: int
    value: dict


class SensorReadingUpdateSchema(BaseModel):
    sensor_id: int
    value: dict
