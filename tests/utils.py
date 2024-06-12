from fastapi.testclient import TestClient

from src.main import app
from src.middleware import auth

client = TestClient(app)


async def override_validate():
    return True


app.dependency_overrides[auth.validate] = override_validate
