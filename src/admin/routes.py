from fastapi import APIRouter
from fastcrud import FastCRUD
from src.admin import models
from src.admin import schemas
from src.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

router = APIRouter()
api_key_crud = FastCRUD(models.APIKey)


@router.post("/create")
async def create(db: AsyncSession = Depends(get_session)):
    api_key = schemas.APIKeyCreateSchema(key="test", user_id=1)
    return await api_key_crud.create(db, api_key)
