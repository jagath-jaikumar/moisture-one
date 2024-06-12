from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    email: str


class UserUpdateSchema(BaseModel):
    name: str
    email: str


class APIKeyCreateSchema(BaseModel):
    key: str
    user_id: int
