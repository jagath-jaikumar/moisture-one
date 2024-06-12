from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from fastapi import FastAPI
from sqlalchemy.pool import NullPool

from src.db.base import Base
from src.settings import settings
from uuid import uuid4


connection_string = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_database}"

# https://github.com/supabase/supavisor/issues/287
engine = create_async_engine(
    connection_string,
    poolclass=NullPool,
    connect_args={
        "prepared_statement_name_func": lambda: f"__asyncpg_{uuid4()}__",
        "statement_cache_size": 0,
        "prepared_statement_cache_size": 0,
    },
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Database session dependency
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# Create tables before the app start
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
