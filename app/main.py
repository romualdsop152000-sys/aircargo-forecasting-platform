from fastapi import FastAPI

from app.database import engine, Base
from app.models import Prediction, Flight
from app.routes.prediction import router as prediction_router

from prometheus_fastapi_instrumentator import Instrumentator


try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Database initialization skipped: {e}")

app = FastAPI(
    title="AirCargo Forecast API",
    description="MLOps project for air cargo demand forecasting",
    version="1.0.0"
)

Instrumentator().instrument(app).expose(app)

app.include_router(prediction_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AirCargo Forecast API",
        "docs": "/docs"
    }