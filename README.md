# ✈️ AirCargo Forecasting Platform

A production-oriented MLOps/Data Engineering platform for real-time air cargo monitoring and forecasting using FastAPI, PostgreSQL, Redis, Prometheus, and Grafana.

---

![Build](https://img.shields.io/github/actions/workflow/status/romualdleo/aircargo-forecasting/ci.yml?branch=main)
![Coverage](https://img.shields.io/codecov/c/github/romualdleo/aircargo-forecasting)
![License](https://img.shields.io/github/license/romualdleo/aircargo-forecasting)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

---

# 🚀 Project Overview

This project simulates a modern data platform capable of:

* ingesting real-time flight data from the OpenSky API,
* storing and querying flight information,
* exposing REST APIs for predictions and analytics,
* caching responses with Redis,
* monitoring services with Prometheus and Grafana,
* testing APIs with pytest,
* containerizing the entire stack using Docker Compose.

The platform is designed with scalable MLOps and Data Engineering practices in mind.

---

# 🏗️ Architecture

```text
                              ┌──────────────────┐
                              │  OpenSky API     │
                              └────────┬─────────┘
                                           │
                                           ▼
                           ┌────────────────────┐
                           │  Ingestion Service │
                           └────────┬───────────┘
                                        │
                                        ▼
                           ┌────────────────────┐
                           │   PostgreSQL DB    │
                           └────────┬───────────┘
                                        │
               ┌────────────────┴────────────────┐
               ▼                                 ▼
 ┌────────────────┐               ┌────────────────┐
 │ FastAPI API    │               │ Redis Cache    │
 └───────┬────────┘               └────────────────┘
             │
             ▼
 ┌──────────────────────┐
 │ Prometheus Metrics   │
 └─────────┬────────────┘
                ▼
 ┌──────────────────────┐
 │ Grafana Dashboards   │
 └──────────────────────┘
```

---

# ⚙️ Tech Stack

| Category         | Technologies            |
| ---------------- | ----------------------- |
| Backend API      | FastAPI                 |
| Database         | PostgreSQL              |
| Cache            | Redis                   |
| Monitoring       | Prometheus + Grafana    |
| Testing          | pytest                  |
| ORM              | SQLAlchemy              |
| Containerization | Docker + Docker Compose |
| Data Source      | OpenSky Network API     |
| Language         | Python 3.11+            |

---

# 📁 Project Structure

```text
aircargo-forecasting/
│
├── app/
│   ├── routes/
│   ├── ml/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── main.py
│
├── monitoring/
│   └── prometheus.yml
│
├── scripts/
│   └── ingest_opensky.py
│
├── tests/
│   └── test_api.py
│
├── compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 📡 API Endpoints

## Root Endpoint

```http
GET /
```

Response:

```json
{
   "message": "Welcome to AirCargo Forecast API"
}
```

---

## Flight Predictions

```http
POST /predict
```

Request:

```json
{
   "route": "Paris-Dubai",
   "origin": "France",
   "destination": "Dubai"
}
```

---

## Latest Flights

```http
GET /flights?limit=10
```

---

## Metrics

```http
GET /metrics
```

Prometheus metrics endpoint.

---

# 📊 Monitoring

The platform includes:

* Prometheus metrics collection
* Grafana dashboards
* Request monitoring
* API latency monitoring
* Redis cache metrics
* Prediction counters

## Example Metrics

```text
http_requests_total
http_request_duration_seconds
aircargo_predictions_total
aircargo_flights_cache_hits_total
aircargo_flights_cache_misses_total
```

---

# 🧪 Automated Testing

The project uses pytest for API testing.

## Run tests

```bash
pytest
```

## Tested Endpoints

* `/`
* `/metrics`
* `/flights`
* `/predict`

---

# 🐳 Docker Deployment

## Start the platform

```bash
docker compose up --build
```

## Available Services

| Service      | URL                                                      |
| ------------ | -------------------------------------------------------- |
| FastAPI      | [http://localhost:8000](http://localhost:8000)           |
| Swagger Docs | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Prometheus   | [http://localhost:9090](http://localhost:9090)           |
| Grafana      | [http://localhost:3000](http://localhost:3000)           |
| PostgreSQL   | localhost:5432                                           |
| Redis        | localhost:6379                                           |

---

# 📈 Current Features

## ✅ Completed

* FastAPI REST API
* PostgreSQL integration
* OpenSky ingestion pipeline
* Redis caching
* Prometheus metrics
* Grafana dashboards
* Docker Compose infrastructure
* Automated tests with pytest

## 🚧 Planned Features

* JWT Authentication
* MLflow experiment tracking
* Kubernetes deployment
* CI/CD GitHub Actions
* Cloud deployment (AWS/GCP/Render)
* Background task orchestration

---

# 🔒 Future Improvements

## Authentication

JWT-based authentication for secured endpoints.

## MLOps

* MLflow experiment tracking
* model versioning
* automated retraining

## Scalability

* Kubernetes orchestration
* horizontal scaling
* CI/CD pipelines

---

# 📷 Screenshots

## Swagger API

*Add Swagger screenshot here.*

## Grafana Dashboard

*Add Grafana dashboard screenshot here.*

---

# 👨‍💻 Author

**Romuald Leo**

PhD in Physics • AI & MLOps Engineering • Data Engineering • Quantum Technologies

---

# ⭐ Project Goals

This project aims to demonstrate:

* production-ready API development,
* real-time data ingestion,
* monitoring and observability,
* scalable MLOps architecture,
* containerized infrastructure,
* testing and automation best practices.
