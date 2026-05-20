import json
import os
from datetime import datetime

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import Flight


def run_ingestion() -> int:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/aircargo"
    )

    engine = create_engine(DATABASE_URL)

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    with open("credentials.json", "r") as f:
        creds = json.load(f)

    client_id = creds["leoromix@gmail.com-api-client"]
    client_secret = creds["leoromix@gmail.com-api-secret"]

    token_url = (
        "https://auth.opensky-network.org/auth/realms/"
        "opensky-network/protocol/openid-connect/token"
    )

    response = requests.post(
        token_url,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )

    if response.status_code != 200:
        print("Erreur récupération token:", response.status_code)
        print(response.text)
        return 0

    access_token = response.json()["access_token"]

    print("Token retrieved successfully")

    url = "https://opensky-network.org/api/states/all"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "lamin": 41.0,
        "lamax": 51.5,
        "lomin": -5.0,
        "lomax": 9.5,
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
    )

    if response.status_code != 200:
        print("Erreur API OpenSky:", response.status_code)
        print(response.text)
        return 0

    data = response.json()
    states = data.get("states", [])

    print(f"Number of flights retrieved: {len(states)}")

    db = SessionLocal()

    try:
        for flight in states:
            new_flight = Flight(
                icao24=flight[0],
                callsign=flight[1].strip() if flight[1] else None,
                origin_country=flight[2],
                longitude=flight[5],
                latitude=flight[6],
                altitude=flight[7],
                velocity=flight[9],
                collected_at=datetime.utcnow(),
            )

            db.add(new_flight)

        db.commit()

        print(f"{len(states)} flights inserted into PostgreSQL")

        return len(states)

    except Exception as e:
        db.rollback()
        print(f"Erreur insertion PostgreSQL: {e}")
        return 0

    finally:
        db.close()


if __name__ == "__main__":
    run_ingestion()