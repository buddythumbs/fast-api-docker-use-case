from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Gather the environment variables for connecting to db(defined in the docker-compose.yml)
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD", '')
POSTGRES_HOST=os.environ.get("POSTGRES_SERVICE", '')
POSTGRES_PORT=os.environ.get("POSTGRES_PORT", 5432)
DB_NAME=os.environ.get("DB_NAME", '')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()