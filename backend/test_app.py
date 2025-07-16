# backend/test_app.py

from fastapi.testclient import TestClient
from main import app, memory_db

client = TestClient(app)


def setup_function():
    # Réinitialise la DB avant chaque test
    memory_db["fruits"] = []

def test_get_fruits_empty():
    response = client.get("/fruits")
    assert response.status_code == 200
    data = response.json()
    assert data == {"fruits": []}

def test_post_fruit():
    fruit_payload = {"name": "mango"}
    response = client.post("/fruits", json=fruit_payload)
    assert response.status_code == 200

    # La réponse doit être un objet Fruit, pas Fruits
    data = response.json()
    assert data == {"fruits":[{"name": "mango"}]}

    # Vérifie que le fruit est bien ajouté dans GET
    response = client.get("/fruits")
    data = response.json()
    assert data == {"fruits": [{"name": "mango"}]}