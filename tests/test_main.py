from tests.utils import client


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Moisture One API"'


def test_read_liveness():
    response = client.get("/liveness")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_validate_token():
    response = client.get("/validate")
    assert response.status_code == 200
    assert response.json() == {"token": "valid"}
