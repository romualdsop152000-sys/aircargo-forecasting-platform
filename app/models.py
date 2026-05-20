from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    route = Column(String, nullable=False)
    origin = Column(String, nullable=True)
    destination = Column(String, nullable=True)
    predicted_demand = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Flight(Base):
    __tablename__ = "flights"
    
    id = Column(Integer, primary_key=True, index=True)
    icao24 = Column(String, index=True)
    callsign = Column(String, nullable=True)
    origin_country = Column(String, nullable=True)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    altitude = Column(Float, nullable=True)
    velocity = Column(Float, nullable=True)
    collected_at = Column(DateTime, default=datetime.utcnow)
    