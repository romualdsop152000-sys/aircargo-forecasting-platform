import os
from datetime import datetime

import requests

from app.database import SessionLocal
from app.models import Flight


OPENSKY_URL = "https://opensky-network.org/api/states/all"


def fetch_opensky_states(limit: int = 50):
    response = requests.get(OPENSKY_URL, timeout=20)
    response.raise_for_status()

    data = response.json()
    states = data.get("states", [])

    if not states:
        return []

    return states[:limit]


def save_flights(states):
    db = SessionLocal()
    saved = 0

    try:
        for state in states:
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

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

    return saved


def collect_flights(limit: int = 50):
    states = fetch_opensky_states(limit=limit)
    saved = save_flights(states)

    print(f"Collected {saved} flights from OpenSky")

    return saved


if __name__ == "__main__":
    limit = int(os.getenv("OPENSKY_LIMIT", 50))
    collect_flights(limit=limit)