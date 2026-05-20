import json
from app.cache import redis_client

from fastapi import  APIRouter, Depends
from sqlalchemy.orm import Session
from app.metrics import PREDICTIONS_TOTAL

from app.metrics import (
    PREDICTIONS_TOTAL,
    FLIGHTS_CACHE_HITS,
    FLIGHTS_CACHE_MISSES
)

from app.ml.predictor import predict_demand

from app.database import SessionLocal
from app.schemas import PredictionRequest, PredictionResponse, FlightResponse
from app.crud import create_prediction, get_all_predictions, get_latest_flights

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    predicted_demand = predict_demand(
        origin_country=request.origin or "France",
        altitude=10000.0,
        velocity=220.0
    )

    prediction = create_prediction(
        db=db,
        route=request.route,
        origin=request.origin,
        destination=request.destination,
        predicted_demand=predicted_demand
    )
    
    PREDICTIONS_TOTAL.inc()

    return prediction


@router.get("/predictions", response_model=list[PredictionResponse])
def list_predictions(db: Session = Depends(get_db)):
    return get_all_predictions(db)


@router.get("/flights", response_model=list[FlightResponse])
def list_flights(limit: int = 50, db: Session = Depends(get_db)):
    cache_key = f"latest_flights:{limit}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        FLIGHTS_CACHE_HITS.inc()
        return json.loads(cached_data)

    FLIGHTS_CACHE_MISSES.inc()

    flights = get_latest_flights(db, limit)

    result = [
        FlightResponse.model_validate(flight).model_dump(mode="json")
        for flight in flights
    ]

    redis_client.setex(cache_key, 60, json.dumps(result))

    return result
