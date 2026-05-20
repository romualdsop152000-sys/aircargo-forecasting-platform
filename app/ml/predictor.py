from datetime import datetime

import joblib
import pandas as pd


model = joblib.load("app/ml/model.pkl")
encoder = joblib.load("app/ml/encoder.pkl")


def predict_demand(origin_country: str, altitude: float, velocity: float) -> float:
    hour = datetime.utcnow().hour

    if origin_country in encoder.classes_:
        country_encoded = encoder.transform([origin_country])[0]
    else:
        country_encoded = 0

    X = pd.DataFrame(
        [{
            "country_encoded": country_encoded,
            "altitude": altitude,
            "velocity": velocity,
            "hour": hour,
        }]
    )

    prediction = model.predict(X)[0]

    return round(float(prediction), 2)