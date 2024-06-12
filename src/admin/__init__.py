from fastcrud import crud_router
from src.admin import schemas
from src.admin import models
from src.admin import routes
from src.db import get_session
from fastapi import APIRouter

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
router.include_router(routes.router, prefix="/api-key", tags=["API Key"])
