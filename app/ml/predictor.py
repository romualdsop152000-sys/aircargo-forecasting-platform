import os
import random
from datetime import datetime

import mlflow


MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "file:/tmp/mlruns")
MLFLOW_EXPERIMENT_NAME = "aircargo-demand-prediction"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


def predict_demand(origin_country: str, altitude: float, velocity: float):
    experiment = mlflow.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)

    if experiment is None:
        experiment_id = mlflow.create_experiment(MLFLOW_EXPERIMENT_NAME)
    else:
        experiment_id = experiment.experiment_id

    run_name = f"{origin_country}-alt{int(altitude)}-vel{int(velocity)}"

    with mlflow.start_run(
        experiment_id=experiment_id,
        run_name=run_name
    ):
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