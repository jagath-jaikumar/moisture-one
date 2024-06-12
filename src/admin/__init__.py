from fastapi import APIRouter
from fastcrud import crud_router

from src.admin import models, schemas
from src.db import get_session

router = APIRouter()


user_router = crud_router(
    session=get_session,
    model=models.User,
    create_schema=schemas.UserCreateSchema,
    update_schema=schemas.UserUpdateSchema,
    path="/user",
    tags=["User"],
)

router.include_router(user_router)
