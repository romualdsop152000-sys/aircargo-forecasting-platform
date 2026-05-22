import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.metrics import FLIGHTS_INGESTED_TOTAL

from app.ingestion.opensky_collector import collect_flights

from app.auth import get_current_user
from app.cache import redis_client
from app.crud import create_prediction, get_all_predictions, get_latest_flights
from app.database import SessionLocal

from app.metrics import (
    PREDICTIONS_TOTAL,
    FLIGHTS_CACHE_HITS,
    FLIGHTS_CACHE_MISSES,
    FLIGHTS_INGESTED_TOTAL,
)

from app.ml.predictor import predict_demand
from app.schemas import PredictionRequest, PredictionResponse, FlightResponse


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/predict", response_model=PredictionResponse)
def predict(
    request: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    predicted_demand = predict_demand(
        origin_country=request.origin or "France",
        altitude=10000.0,
        velocity=220.0,
    )

    prediction = create_prediction(
        db=db,
        route=request.route,
        origin=request.origin,
        destination=request.destination,
        predicted_demand=predicted_demand,
    )

    PREDICTIONS_TOTAL.inc()

    return prediction


@router.get("/predictions", response_model=list[PredictionResponse])
def list_predictions(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return get_all_predictions(db)

@router.post("/ingest/flights")
def ingest_flights(
    limit: int = 30,
    current_user: dict = Depends(get_current_user),
):
    try:
        saved = collect_flights(limit=limit)

        FLIGHTS_INGESTED_TOTAL.inc(saved)

        return {
            "message": "Real flights collected successfully from OpenSky",
            "saved": saved,
        }

    except Exception as e:
        print(f"Flight ingestion failed: {e}")

        raise HTTPException(
            status_code=503,
            detail=str(e),
        )


@router.get("/flights", response_model=list[FlightResponse])
def list_flights(limit: int = 50, db: Session = Depends(get_db)):
    cache_key = f"latest_flights:{limit}"

    try:
        if redis_client is not None:
            cached_data = redis_client.get(cache_key)

            if cached_data:
                FLIGHTS_CACHE_HITS.inc()
                return json.loads(cached_data)

    except Exception as e:
        print(f"Redis cache unavailable: {e}")

    FLIGHTS_CACHE_MISSES.inc()

    flights = get_latest_flights(db, limit)

    result = [
        FlightResponse.model_validate(flight).model_dump(mode="json")
        for flight in flights
    ]

    try:
        if redis_client is not None:
            redis_client.setex(cache_key, 60, json.dumps(result))
    except Exception as e:
        print(f"Redis cache write skipped: {e}")

    return result
