from typing import Union

from fastapi import FastAPI, Depends

from src.settings import settings
from src.utils.sentry import init as sentry_init
from src.fleet import router as fleet_router
from src.admin import router as admin_router
from src.middleware import auth


sentry_init(settings)
app = FastAPI()

app.include_router(fleet_router, prefix="/api", dependencies=[Depends(auth.validate)])
app.include_router(admin_router, prefix="/admin", dependencies=[Depends(auth.validate)])


@app.get("/")
def root():
    return "Moisture One API"
