import os
from datetime import datetime

import requests

from app.database import SessionLocal
from app.models import Flight


OPENSKY_URL = "https://opensky-network.org/api/states/all"

# Zone France + proches frontières
# Cela réduit fortement le risque de 429 par rapport à une requête globale.
FRANCE_BBOX = {
    "lamin": 41.0,   # latitude min
    "lomin": -5.5,   # longitude min
    "lamax": 51.5,   # latitude max
    "lomax": 9.5,    # longitude max
}


def fetch_opensky_states(limit: int = 20):
    """
    Fetch real aircraft states from OpenSky API.
    No fallback data is used.
    """

    headers = {
        "User-Agent": "AirCargo-Forecasting-Platform/1.0"
    }

    response = requests.get(
        OPENSKY_URL,
        headers=headers,
        params=FRANCE_BBOX,
        timeout=30,
    )

    if response.status_code == 429:
        retry_after = response.headers.get(
            "X-Rate-Limit-Retry-After-Seconds",
            "unknown"
        )

        raise Exception(
            f"OpenSky rate limit reached. Retry after {retry_after} seconds."
        )

    if response.status_code != 200:
        raise Exception(
            f"OpenSky API error: status={response.status_code}, body={response.text[:300]}"
        )

    data = response.json()
    states = data.get("states") or []

    return states[:limit]


def save_flights(states):
    """
    Save OpenSky aircraft states into PostgreSQL.
    """

    db = SessionLocal()
    saved = 0

    try:
        for state in states:
            if not state or len(state) < 10:
                continue

            flight = Flight(
                icao24=state[0],
                callsign=state[1].strip() if state[1] else None,
                origin_country=state[2],
                longitude=state[5],
                latitude=state[6],
                altitude=state[7],
                velocity=state[9],
                collected_at=datetime.utcnow(),
            )

            db.add(flight)
            saved += 1

        db.commit()

    except Exception as e:
        db.rollback()
        raise Exception(f"Database insert error: {str(e)}")

    finally:
        db.close()

    return saved


def collect_flights(limit: int = 20):
    """
    Collect real flight data from OpenSky and persist it.
    """

    states = fetch_opensky_states(limit=limit)

    if not states:
        return 0

    saved = save_flights(states)

    print(f"Collected {saved} real flights from OpenSky")

    return saved


if __name__ == "__main__":
    limit = int(os.getenv("OPENSKY_LIMIT", 20))
    collect_flights(limit=limit)