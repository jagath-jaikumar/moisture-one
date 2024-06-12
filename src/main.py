from typing import Union

from fastapi import FastAPI

from src.db import lifespan
from src.settings import settings
from src.utils.sentry import init as sentry_init

sentry_init(settings)
app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return "Moisture One API"
