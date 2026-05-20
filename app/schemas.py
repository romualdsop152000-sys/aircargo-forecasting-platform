from datetime import datetime
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    route: str
    origin: str | None = None
    destination: str | None = None
    

class PredictionResponse(BaseModel):
    id: int
    route: str
    origin: str | None = None
    destination: str | None = None
    predicted_demand: float
    created_at: datetime
    
    class Config:
        from_attributes = True
        
        
class FlightResponse(BaseModel):
    id: int
    icao24: str | None = None
    callsign: str | None = None
    origin_country: str | None = None
    longitude: float | None = None
    latitude: float | None = None
    altitude: float | None = None
    velocity: float | None = None
    collected_at: datetime

    class Config:
        from_attributes = True