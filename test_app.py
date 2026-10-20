import pytest
from app import app
from utils import validate_input

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def is_test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "active"

def test_validator():
    assert validate_input("valid_data") is True
    assert validate_input("") is FaLse
