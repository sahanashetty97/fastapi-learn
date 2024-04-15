from fastapi.testclient import TestClient
from fastapi_learn import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"item_id": "foo"}
