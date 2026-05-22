# ✈️ AirCargo Forecasting Platform

![CI](https://github.com/romualdsop152000-sys/aircargo-forecasting-platform/actions/workflows/ci.yml/badge.svg)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange)
![Grafana](https://img.shields.io/badge/Grafana-Cloud_Dashboard-F46800)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF)
![JWT](https://img.shields.io/badge/Auth-JWT-black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**AirCargo Forecasting Platform** is a production-oriented **MLOps, Data Engineering and Backend API** project designed to simulate and monitor an air cargo demand forecasting platform.

The project demonstrates how to build a modern cloud-native backend around a machine learning prediction service, including:

- FastAPI backend API
- JWT authentication
- PostgreSQL persistence
- Redis caching
- MLflow experiment tracking
- OpenSky flight data ingestion
- Prometheus metrics
- Grafana Cloud dashboards
- Docker containerization
- Kubernetes local orchestration
- GitHub Actions CI/CD
- Render cloud deployment

The platform is designed as a portfolio-level project for **Data Engineering**, **MLOps**, **AI Engineering**, **Backend ML Engineering** and **Cloud AI Engineering** roles.

---

## 🎯 Project Objectives

The main objective of this project is to build a realistic end-to-end platform combining:

- API development
- Machine learning prediction serving
- Experiment tracking
- Database persistence
- External data ingestion
- Cache optimization
- Monitoring and observability
- CI/CD automation
- Containerization
- Kubernetes orchestration
- Cloud deployment

This project goes beyond a simple API by integrating several production-oriented components commonly used in real-world MLOps and data platforms.

---

## 🧠 Use Case

The platform simulates an **air cargo demand forecasting workflow**.

A user can:

1. Authenticate using JWT.
2. Submit a cargo route prediction request.
3. Receive a predicted air cargo demand.
4. Store the prediction in PostgreSQL.
5. Track the prediction run in MLflow.
6. Ingest real flight data from the OpenSky API.
7. Retrieve the latest ingested flights through a cached API endpoint.
8. Monitor API traffic, latency, predictions, cache behavior and system resources using Prometheus and Grafana Cloud.

---

## 🏗️ Global Architecture

```text
                         +----------------------+
                         |        Client        |
                         | Swagger / Browser    |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |      FastAPI API     |
                         |  JWT / REST / ML API |
                         +----------+-----------+
                                    |
        -----------------------------------------------------
        |                  |                  |              |
        v                  v                  v              v
+---------------+   +---------------+   +---------------+   +----------------+
|  PostgreSQL   |   |     Redis     |   |    MLflow     |   |  Prometheus    |
| Predictions   |   | Cache Layer   |   | Tracking      |   | Metrics Scrape |
| Flights       |   | /flights      |   | Experiments   |   | /metrics       |
+---------------+   +---------------+   +---------------+   +----------------+
                                                                 |
                                                                 v
                                                        +----------------+
                                                        | Grafana Cloud  |
                                                        | Dashboards     |
                                                        +----------------+
```

---

## 🔄 Main Workflows

### Prediction Workflow

```text
User
 ↓
POST /login
 ↓
JWT Token
 ↓
POST /predict
 ↓
FastAPI calls predict_demand()
 ↓
Prediction stored in PostgreSQL
 ↓
MLflow logs parameters and metrics
 ↓
Prometheus collects API metrics
 ↓
Grafana Cloud visualizes activity
```

### Flight Data Ingestion Workflow

```text
GitHub Actions Scheduler / Swagger
 ↓
POST /ingest/flights
 ↓
OpenSky API
 ↓
Real aircraft states collected
 ↓
Flight data saved in PostgreSQL
 ↓
GET /flights
 ↓
Redis cache layer
 ↓
Prometheus metrics
 ↓
Grafana Cloud dashboard
```

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| Programming Language | Python 3.11 |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Cache | Redis |
| ML Tracking | MLflow |
| Monitoring | Prometheus |
| Dashboards | Grafana Cloud |
| Authentication | JWT |
| Testing | Pytest |
| Containerization | Docker |
| Local Orchestration | Kubernetes with Kind |
| CI/CD | GitHub Actions |
| Cloud Deployment | Render |
| External Data Source | OpenSky API |

---

## ✨ Features

### Backend API

- REST API built with FastAPI
- Swagger/OpenAPI documentation
- JWT authentication
- Protected prediction endpoint
- Prediction history endpoint
- Flight data retrieval endpoint
- Prometheus-compatible `/metrics` endpoint

### Machine Learning / MLOps

- Air cargo demand prediction endpoint
- MLflow experiment creation
- MLflow run tracking
- Parameter logging
- Metric logging
- Cloud MLflow deployment on Render

### Data Engineering

- OpenSky API flight ingestion
- PostgreSQL persistence for flight data
- Scheduled ingestion using GitHub Actions
- `/flights` endpoint for retrieving latest ingested flights

### Caching

- Redis caching for `/flights`
- Cache hit and miss counters
- Graceful fallback when Redis is unavailable

### Monitoring & Observability

- Prometheus metrics endpoint
- API request monitoring
- HTTP status tracking
- API latency monitoring
- Prediction counters
- Redis cache metrics
- Flight ingestion metrics
- System metrics
- Grafana Cloud dashboards

### DevOps

- Dockerized FastAPI service
- Docker Compose support
- Kubernetes manifests
- GitHub Actions CI/CD pipeline
- Render cloud deployment

---

## 🔐 Authentication

The API uses JWT authentication.

### Login Endpoint

```http
POST /login
```

Form data:

```text
username=admin
password=admin123
grant_type=password
```

Example response:

```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

Use the token in Swagger through the **Authorize** button:

```text
Bearer <token>
```

---

## 📡 API Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---:|---|
| GET | `/` | No | Welcome endpoint |
| GET | `/docs` | No | Swagger/OpenAPI documentation |
| POST | `/login` | No | JWT authentication |
| POST | `/predict` | Yes | Predict air cargo demand |
| GET | `/predictions` | Yes | List stored predictions |
| GET | `/flights` | No | List latest ingested flights |
| POST | `/ingest/flights` | Yes | Ingest real flight data from OpenSky |
| GET | `/metrics` | No | Prometheus metrics endpoint |

---

## 🧪 Prediction Example

### Request

```json
{
  "route": "Paris-Dubai",
  "origin": "France",
  "destination": "Dubai"
}
```

### Response

```json
{
  "id": 1,
  "route": "Paris-Dubai",
  "origin": "France",
  "destination": "Dubai",
  "predicted_demand": 3594.45,
  "created_at": "2026-05-21T18:35:23"
}
```

---

## 🛫 Flight Ingestion

The platform includes an ingestion pipeline that collects real aircraft state data from the OpenSky API.

### Manual ingestion

```http
POST /ingest/flights?limit=10
```

This endpoint:

1. Calls OpenSky API.
2. Retrieves real aircraft states.
3. Stores selected flight data into PostgreSQL.
4. Updates Prometheus ingestion metrics.

### Retrieve latest flights

```http
GET /flights?limit=5
```

Example response:

```json
[
  {
    "id": 1,
    "icao24": "394c13",
    "callsign": "AFR123",
    "origin_country": "France",
    "longitude": 2.55,
    "latitude": 49.01,
    "altitude": 11000.0,
    "velocity": 230.0,
    "collected_at": "2026-05-21T20:00:00"
  }
]
```

---

## 🧬 MLflow Tracking

MLflow is used to track each prediction run.

For every prediction, the platform logs:

### Parameters

- `origin_country`
- `altitude`
- `velocity`

### Metrics

- `predicted_demand`

### Run name example

```text
France-alt10000-vel220
```

MLflow is deployed as a dedicated Render service.

Example tracking URI:

```text
https://aircargo-mlflow.onrender.com
```

---

## 📈 Prometheus Metrics

FastAPI exposes metrics through:

```http
GET /metrics
```

### Main Application Metrics

| Metric | Description |
|---|---|
| `aircargo_predictions_total` | Total number of ML predictions |
| `aircargo_flights_ingested_total` | Total number of flights ingested from OpenSky |
| `aircargo_flights_cache_hits_total` | Total Redis cache hits for `/flights` |
| `aircargo_flights_cache_misses_total` | Total Redis cache misses for `/flights` |
| `http_requests_total` | Total HTTP requests by endpoint, method and status |
| `http_request_duration_seconds` | API latency by endpoint |
| `process_resident_memory_bytes` | Memory usage |
| `process_cpu_seconds_total` | CPU usage |
| `python_gc_collections_total` | Python garbage collection metrics |

---

## 📊 Grafana Cloud Dashboard

Grafana Cloud is used to visualize Prometheus metrics.

### Dashboard Sections

- API overview
- ML predictions
- Latency and performance
- Redis cache behavior
- OpenSky ingestion pipeline
- System resources
- Python runtime metrics

### Recommended Panels

| Panel | Visualization | Query |
|---|---|---|
| Total ML Predictions | Stat | `aircargo_predictions_total` |
| Total Flights Ingested | Stat | `aircargo_flights_ingested_total` |
| API Requests Rate by Endpoint | Time series | `sum by (handler) (rate(http_requests_total[1m]))` |
| HTTP Status Distribution | Pie chart | `sum by (status) (http_requests_total)` |
| Average Latency by Endpoint | Time series | `sum by (handler) (rate(http_request_duration_seconds_sum[1m])) / sum by (handler) (rate(http_request_duration_seconds_count[1m]))` |
| Ingestion HTTP Status Distribution | Pie chart | `sum by (status) (http_requests_total{handler="/ingest/flights"})` |
| Redis Cache Hit Ratio | Gauge | `aircargo_flights_cache_hits_total / clamp_min(aircargo_flights_cache_hits_total + aircargo_flights_cache_misses_total, 1)` |
| Memory Usage | Time series | `process_resident_memory_bytes` |
| CPU Usage | Time series | `rate(process_cpu_seconds_total[1m])` |

---

## ⚙️ Environment Variables

### FastAPI Service

```env
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
MLFLOW_TRACKING_URI=https://aircargo-mlflow.onrender.com
SECRET_KEY=your_secret_key
```

### MLflow Service

```env
DATABASE_URL=postgresql://...
```

### Grafana on Render, optional

Grafana Cloud is recommended for persistence.

If using Grafana on Render, configure:

```env
GF_SERVER_HTTP_PORT=10000
GF_SERVER_ROOT_URL=https://aircargo-grafana.onrender.com
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin123
GF_PATHS_DATA=/var/lib/grafana
```

---

## 🐳 Docker

### Build image

```bash
docker build -t aircargo-api .
```

### Run with Docker Compose

```bash
docker compose up --build
```

Docker Compose can run:

- FastAPI API
- PostgreSQL
- Redis
- MLflow

---

## ☸️ Kubernetes Local Deployment

The project includes Kubernetes manifests for local orchestration with Kind.

### Create cluster

```bash
kind create cluster --name aircargo
```

### Apply manifests

```bash
kubectl apply -f k8s/
```

### Check resources

```bash
kubectl get pods -n aircargo
kubectl get svc -n aircargo
```

### API port-forward

```bash
kubectl port-forward -n aircargo deployment/aircargo-api 8081:8000
```

Access Swagger locally:

```text
http://localhost:8081/docs
```

### MLflow port-forward

```bash
kubectl port-forward -n aircargo svc/mlflow 5001:5000
```

Access MLflow locally:

```text
http://localhost:5001
```

---

## 🔄 CI/CD with GitHub Actions

The project uses GitHub Actions for continuous integration.

The CI pipeline:

- Installs dependencies
- Runs Pytest
- Validates the FastAPI app
- Tests API endpoints
- Verifies Redis fallback behavior
- Ensures prediction routes work with JWT authentication

Workflow file:

```text
.github/workflows/ci.yml
```

### Run tests locally

```bash
pytest
```

---

## ⏱️ Scheduled Flight Ingestion

A GitHub Actions scheduled workflow can trigger flight ingestion automatically.

Workflow file:

```text
.github/workflows/ingest-flights.yml
```

Example schedule:

```yaml
on:
  schedule:
    - cron: "0 */6 * * *"
  workflow_dispatch:
```

The workflow:

1. Wakes up the Render API.
2. Logs in to retrieve a JWT token.
3. Calls `/ingest/flights`.
4. Stores OpenSky flight data in PostgreSQL.

Required GitHub secrets:

```text
API_USERNAME
API_PASSWORD
```

---

## 📁 Project Structure

```text
aircargo-forecasting-platform/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── cache.py
│   ├── metrics.py
│   │
│   ├── routes/
│   │   └── prediction.py
│   │
│   ├── ml/
│   │   └── predictor.py
│   │
│   └── ingestion/
│       ├── __init__.py
│       └── opensky_collector.py
│
├── tests/
│   └── test_api.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── api-deployment.yaml
│   ├── api-service.yaml
│   ├── postgres-deployment.yaml
│   ├── redis-deployment.yaml
│   └── mlflow-deployment.yaml
│
├── monitoring/
│   ├── prometheus-render/
│   │   ├── Dockerfile
│   │   └── prometheus.yml
│   │
│   └── grafana/
│       └── dashboards/
│           └── aircargo-dashboard.json
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── ingest-flights.yml
│
├── Dockerfile
├── compose.yml
├── requirements.txt
└── README.md
```

---

## 🌐 Cloud Deployment

The platform is deployed on Render and Grafana Cloud.

### Services

| Service | Platform | Role |
|---|---|---|
| `aircargo-forecasting-platform` | Render Web Service | FastAPI API |
| `aircargo-mlflow` | Render Web Service | MLflow tracking server |
| PostgreSQL | Render Managed Database | Persistence |
| Redis | Render Key Value | Cache |
| `aircargo-prometheus` | Render Docker Web Service | Metrics scraping |
| Grafana Cloud | Grafana Cloud | Dashboards |

---

## 🔗 Live URLs

| Service | URL |
|---|---|
| FastAPI Swagger | `https://aircargo-forecasting-platform.onrender.com/docs` |
| MLflow | `https://aircargo-mlflow.onrender.com` |
| Prometheus | `https://aircargo-prometheus.onrender.com` |
| Grafana Cloud | `Add your Grafana Cloud URL here` |

---

## 📸 Screenshots & Walkthrough

This section documents the main components of the platform with real screenshots.

### 1. Swagger / OpenAPI

FastAPI automatically provides interactive API documentation.

![Swagger 1](docs/images/swagger_1.png)

![Swagger 2](docs/images/swagger_2.png)

![Swagger 3](docs/images/swagger_3.png)

![Swagger 4](docs/images/swagger_4.png)

![Swagger 5](docs/images/swagger_5.png)

![Swagger 6](docs/images/swagger_6.png)

![Swagger 7](docs/images/swagger_7.png)

---

### 2. MLflow Experiment Tracking

MLflow tracks prediction runs, parameters and metrics.

![MLflow 1](docs/images/mlflow_1.png)

![MLflow 2](docs/images/mlflow_2.png)

---

### 3. Prometheus Monitoring

Prometheus scrapes the FastAPI `/metrics` endpoint.

![Prometheus Target](docs/images/Promotheus.png)

![Prometheus Graph](docs/images/Promotheus_1.PNG)

---

### 4. Grafana Cloud Dashboard

Grafana Cloud visualizes API, ML, cache, ingestion and system metrics.

![Grafana](docs/images/grafana.png)

---

### 5. GitHub Actions CI/CD

GitHub Actions validates the project on every push.

![GitHub Actions](docs/images/github-actions.png)

---

### 6. Kubernetes Local Deployment

Kubernetes manifests allow local orchestration with Kind.

![K8s Pods](docs/images/k8s_1.png)

![K8s Services](docs/images/k8s_2.png)

---

## 🧪 Testing Summary

The test suite validates:

- Home endpoint
- Metrics endpoint
- Flights endpoint
- Prediction endpoint without token
- Prediction endpoint with JWT token
- Redis optional fallback through mocks
- Prediction function mocking

Run tests:

```bash
pytest
```

---

## 🧩 Key Engineering Challenges Solved

### Redis on Render

Redis was made optional with a graceful fallback to avoid API failures when Redis is unavailable.

### MLflow Cloud Tracking

MLflow was configured to create experiments dynamically and log runs remotely from FastAPI.

### OpenSky API Rate Limits

The ingestion pipeline was adjusted to use a limited geographical bounding box and slower scheduled ingestion to reduce rate-limit issues.

### Grafana Persistence

Grafana Cloud was adopted to avoid dashboard loss caused by non-persistent storage on free Render services.

### CI/CD Reliability

Tests were adapted to mock Redis when `REDIS_URL` is absent in GitHub Actions.

### Prometheus on Render

Prometheus was deployed as a dedicated Docker service on Render and configured to scrape the FastAPI `/metrics` endpoint over HTTPS.

---

## 🚧 Future Improvements

Planned improvements:

- Train and serve a real ML model instead of simulated prediction logic
- Add MLflow Model Registry
- Add model versioning
- Add Airflow or Prefect orchestration
- Add feature engineering pipeline
- Add batch training pipeline
- Add model drift monitoring
- Add OpenSky authentication for higher API rate limits
- Add PostgreSQL migrations with Alembic
- Add Helm charts for Kubernetes deployment
- Add cloud deployment on AWS or GCP
- Add a frontend dashboard
- Add alerting rules in Grafana Cloud
- Add alert notifications through Slack or email
- Add API rate limiting and security hardening

---

## 👨‍💻 Author

**Romuald Leo**

PhD Physics • AI & MLOps Engineer  
Specialized in scientific computing, data engineering, machine learning infrastructure and cloud-native AI systems.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Portfolio Value

This project demonstrates a complete production-oriented MLOps and Data Engineering architecture including:

- API design
- Cloud deployment
- Authentication
- Data persistence
- External data ingestion
- ML experiment tracking
- Real-time monitoring
- Dashboarding
- CI/CD
- Containerization
- Kubernetes orchestration

It is especially relevant for roles such as:

- Data Engineer
- MLOps Engineer
- AI Engineer
- Backend ML Engineer
- Cloud AI Engineer
- Platform Engineer
