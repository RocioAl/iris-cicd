from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["prediction"] == 0
    assert body["species"] == "Iris setosa"
    assert "confidence" in body
    assert "confidence_level" in body


def test_predict_invalid_input():
    payload = {
        "sepal_length": -5.0,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
