from sqlalchemy.orm import Session


from app import models


def create_prediction(
    db: Session,
    route: str,
    origin: str,
    destination: str,
    predicted_demand: float
    ):
     
     prediction = models.Prediction(
         route=route,
         origin=origin,
         destination=destination,
         predicted_demand=predicted_demand
     )
     
     db.add(prediction)
     db.commit()
     db.refresh(prediction)
     
     return prediction
 
def get_all_predictions(db: Session):
     return db.query(models.Prediction).all()
 
 
def get_latest_flights(db: Session, limit: int = 50):
    return (
        db.query(models.Flight)
        .order_by(models.Flight.collected_at.desc())
        .limit(limit)
        .all()
    )