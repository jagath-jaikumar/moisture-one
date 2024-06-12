import os

import requests

MOISTURE_ONE_URL = os.getenv("MOISTURE_ONE_URL", "http://localhost:8000")
MOISTURE_ONE_API_KEY = os.getenv("MOISTURE_ONE_API_KEY")

response = requests.get(f"{MOISTURE_ONE_URL}/liveness")

assert response.status_code == 200

response = requests.get(
    f"{MOISTURE_ONE_URL}/token", headers={"X-API-Key": MOISTURE_ONE_API_KEY}
)

assert response.status_code == 200
