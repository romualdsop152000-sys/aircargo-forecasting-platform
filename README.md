
# ✈️ AirCargo Forecasting Platform
![CI](https://github.com/romualdsop152000-sys/aircargo-forecasting-platform/actions/workflows/ci.yml/badge.svg)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-black)
![License](https://img.shields.io/badge/License-MIT-green)

A complete MLOps-ready Air Cargo Demand Forecasting platform built with:

- FastAPI
- PostgreSQL
- Redis
- MLflow
- Prometheus
- Docker
- Kubernetes (Kind)
- GitHub Actions CI/CD
- JWT Authentication
- Pytest

---

# 🚀 Features

## API

- Air cargo demand prediction
- REST API with FastAPI
- Swagger/OpenAPI documentation
- JWT Authentication

## Data Layer

- PostgreSQL persistence
- Redis caching layer

## MLOps

- MLflow experiment tracking
- Metrics logging
- Parameters tracking
- Kubernetes deployment

## Monitoring

- Prometheus metrics
- API observability

## DevOps

- Docker Compose
- Kubernetes manifests
- GitHub Actions CI/CD
- Automated testing with Pytest

---

# 🏗️ Architecture

```text
                +------------------+
                |     Client       |
                +------------------+
                          |
                          v
                +------------------+
                |    FastAPI API   |
                +------------------+
                  |      |      |
                  |      |      |
                  v      v      v
             PostgreSQL Redis MLflow
                  |
                  v
             Prometheus
```

---

# 📦 Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | PostgreSQL |
| Cache | Redis |
| ML Tracking | MLflow |
| Monitoring | Prometheus |
| Containerization | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Testing | Pytest |

---

# 🔐 Authentication

JWT Authentication is enabled.

## Login Endpoint

```http
POST /login
```

Use:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

---

# ⚙️ Local Development

## Start services

```bash
docker compose up --build
```

## Run API

```bash
uvicorn app.main:app --reload
```

---

# 🧪 Testing

Run tests:

```bash
pytest
```

---

# 📊 MLflow

Start MLflow UI:

```bash
mlflow ui
```

Access:

```text
http://localhost:5000
```

---

# ☸️ Kubernetes Deployment

## Create cluster

```bash
kind create cluster
```

## Deploy

```bash
kubectl apply -f k8s/
```

## Port Forward

API:

```bash
kubectl port-forward -n aircargo deployment/aircargo-api 8081:8000
```

MLflow:

```bash
kubectl port-forward -n aircargo svc/mlflow 5001:5000
```

---

# 📈 Prometheus Metrics

Metrics endpoint:

```text
/metrics
```

---

# 🔄 CI/CD

GitHub Actions automatically:

- installs dependencies
- runs tests
- validates code

Workflow file:

```text
.github/workflows/ci.yml
```

---

# 📁 Project Structure

```text
aircargo-forecasting/
│
├── app/
├── tests/
├── k8s/
├── .github/workflows/
├── Dockerfile
├── compose.yml
├── requirements.txt
└── README.md
```

---



# 📸 Screenshots & Project Walkthrough

Découvrez ci-dessous les principaux composants de la plateforme AirCargo Forecasting, illustrés par des captures réelles du projet en fonctionnement.

## 1. API Documentation (Swagger / OpenAPI)
L’API REST est documentée automatiquement grâce à FastAPI et Swagger. Vous pouvez explorer, tester les endpoints, et visualiser les schémas d’entrée/sortie.

**Exemple d’interface Swagger :**
![Swagger 1](docs/images/swagger_1.png)

**Exemple de formulaire d’authentification :**
![Swagger 2](docs/images/swagger_2.png)

**Réponse d’authentification JWT :**
![Swagger 3](docs/images/swagger_3.png)

**Endpoint de prédiction :**
![Swagger 4](docs/images/swagger_4.png)

**Réponse de prédiction :**
![Swagger 5](docs/images/swagger_5.png)

**Endpoint de listing des vols :**
![Swagger 6](docs/images/swagger_6.png)

**Réponse du listing :**
![Swagger 7](docs/images/swagger_7.png)

---

## 2. MLflow Experiment Tracking
MLflow permet de suivre les expériences de machine learning, les paramètres, les métriques et les résultats de prédiction.


**Vue d’un run MLflow :**
![MLflow 1](docs/images/mlflow_1.png)

**Visualisation des métriques :**
![MLflow 2](docs/images/mlflow_2.png)

---

## 3. Monitoring & Observabilité
La plateforme intègre Prometheus pour la collecte de métriques et Grafana pour la visualisation.


**Cible Prometheus (API FastAPI exposée) :**
![Prometheus Target](docs/images/Promotheus.png)

**Graphique Prometheus :**
![Prometheus Graph](docs/images/Promotheus_1.PNG)

**Dashboard Grafana :**
![Grafana](docs/images/grafana.png)

---

## 4. CI/CD avec GitHub Actions
Chaque push déclenche des tests automatiques, l’installation des dépendances et la validation du code.

**Exemple de workflow réussi :**
![GitHub Actions](docs/images/github-actions.png)

---

## 5. Orchestration Kubernetes
Déploiement multi-services (API, MLflow, Postgres, Redis) sur un cluster local avec Kind.


**Pods déployés :**
![K8s Pods](docs/images/k8s_1.png)

**Services exposés :**
![K8s Services](docs/images/k8s_2.png)

---

# 👨‍💻 Author

Romuald Leo  
PhD Physics • AI & MLOps Engineer

---

# ⭐ Future Improvements

- Real ML model training pipeline
- Grafana dashboards
- Helm charts
- Cloud deployment (AWS/GCP)
- Feature Store
- Airflow orchestration
- Model Registry
