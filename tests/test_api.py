from fastapi.testclient import TestClient

from app.main import app
from app.routes import prediction


client = TestClient(app)


def get_auth_token():
    response = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "admin123",
            "grant_type": "password",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200

    return response.json()["access_token"]


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to AirCargo Forecast API"


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "http_requests_total" in response.text


def test_get_flights(monkeypatch):
    monkeypatch.setattr(prediction.redis_client, "get", lambda key: None)
    monkeypatch.setattr(prediction.redis_client, "setex", lambda key, ttl, value: True)

    monkeypatch.setattr(
        prediction,
        "get_latest_flights",
        lambda db, limit: []
    )

    response = client.get("/flights?limit=5")

    assert response.status_code == 200
    assert response.json() == []


def test_predict_without_token():
    payload = {
        "route": "Paris-Dubai",
        "origin": "France",
        "destination": "Dubai",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 401


def test_predict_with_token(monkeypatch):
    monkeypatch.setattr(
        prediction,
        "predict_demand",
        lambda origin_country, altitude, velocity: 123.45
    )

    fake_prediction = {
        "id": 1,
        "route": "Paris-Dubai",
        "origin": "France",
        "destination": "Dubai",
        "predicted_demand": 123.45,
        "created_at": "2026-05-20T08:00:00",
    }

    monkeypatch.setattr(
        prediction,
        "create_prediction",
        lambda db, route, origin, destination, predicted_demand: fake_prediction
    )

    token = get_auth_token()

    payload = {
        "route": "Paris-Dubai",
        "origin": "France",
        "destination": "Dubai",
    }

    response = client.post(
        "/predict",
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["route"] == "Paris-Dubai"
    assert data["origin"] == "France"
    assert data["destination"] == "Dubai"
    assert data["predicted_demand"] == 123.45