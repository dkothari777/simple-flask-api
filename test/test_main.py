from src.app import app
import pytest

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    yield app.test_client()

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b'Hello World!'