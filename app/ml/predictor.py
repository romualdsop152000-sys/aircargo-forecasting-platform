import os
import random
from datetime import datetime

import mlflow

# Dploiement sur K8s
#mlflow.set_tracking_uri("http://mlflow:5000")

# Pour faire deployer sur render
mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "file:/tmp/mlruns")
)

mlflow.set_experiment("aircargo-demand-prediction")


def predict_demand(origin_country: str, altitude: float, velocity: float):
    run_name = f"{origin_country}-alt{int(altitude)}-vel{int(velocity)}"

    with mlflow.start_run(run_name=run_name):
        mlflow.log_param("origin_country", origin_country)
        mlflow.log_param("altitude", altitude)
        mlflow.log_param("velocity", velocity)

        hour = datetime.utcnow().hour

        base_demand = (
            altitude * 0.1
            + velocity * 5
            + random.uniform(1000, 5000)
        )

        if 6 <= hour <= 18:
            base_demand *= 1.2

        prediction = round(base_demand, 2)

        mlflow.log_metric("predicted_demand", prediction)

        return prediction