from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os
import socket
# Détection automatique du host pour la base de données
if os.getenv("DOCKER_ENV") == "1" or socket.gethostname().startswith("aircargo-forecasting-"):
    db_host = "db"
else:
    db_host = "localhost"
DATABASE_URL = os.getenv("DATABASE_URL", f"postgresql://postgres:password@{db_host}:5432/aircargo")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()