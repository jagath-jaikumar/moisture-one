from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from src.db import async_session
from sqlalchemy import select
from src.admin import models

api_key_header = APIKeyHeader(name="X-API-Key")


async def validate(api_key_header: str = Security(api_key_header)) -> bool:
    if await check_api_key(api_key_header):
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid API key"
    )


async def check_api_key(api_key_header: str):
    session = async_session()
    query = select(models.APIKey).filter_by(key=api_key_header)
    result = await session.execute(query)
    api_key = result.scalar()
    session.close()
    if not api_key:
        return False
    return True
