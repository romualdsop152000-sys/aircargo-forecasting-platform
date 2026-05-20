
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sqlalchemy import create_engine
import os
import socket
# Détection automatique du host pour la base de données
if os.getenv("DOCKER_ENV") == "1" or socket.gethostname().startswith("aircargo-forecasting-"):
    db_host = "db"
else:
    db_host = "localhost"
DATABASE_URL = os.getenv("DATABASE_URL", f"postgresql://postgres:password@{db_host}:5432/aircargo")

engine = create_engine(DATABASE_URL)


# Charger données PostgreSQL
query = """
SELECT
    origin_country,
    altitude,
    velocity,
    EXTRACT(HOUR FROM collected_at) AS hour
FROM flights
WHERE altitude IS NOT NULL
AND velocity IS NOT NULL
"""

df = pd.read_sql(query, engine)

print(df.head())


# Variable cible simulée Traffic score que represente l'activitée aérienne estimée
df["traffic_score"] = (
    df["altitude"] * 0.3
    + df["velocity"] * 0.7
)


# Encoder pays
encoder = LabelEncoder()

df["country_encoded"] = encoder.fit_transform(
    df["origin_country"]
)


# Features
X = df[
    [
        "country_encoded",
        "altitude",
        "velocity",
        "hour"
    ]
]

# Target
y = df["traffic_score"]


# Modèle
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Training
model.fit(X, y)

print("Model trained successfully")


# Sauvegarder modèle
joblib.dump(model, "app/ml/model.pkl")

# Sauvegarder encoder
joblib.dump(encoder, "app/ml/encoder.pkl")

print("Model saved")