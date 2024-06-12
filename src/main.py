from typing import Union

from fastapi import FastAPI

from src.settings import settings
from src.utils.sentry import init as sentry_init
from src.fleet import router as fleet_router
from src.admin import router as admin_router


sentry_init(settings)
app = FastAPI()

app.include_router(fleet_router, prefix="/api")
app.include_router(admin_router, prefix="/admin")


@app.get("/")
def root():
    return "Moisture One API"
