from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_TIMEZONE
import timescaledb

if DATABASE_URL == "":
    raise ValueError("DATABASE_URL is not set in the environment variables")
engine = timescaledb.create_engine(DATABASE_URL, timezone=DB_TIMEZONE)


def init_db():
    print("Database initialized")
    SQLModel.metadata.create_all(engine)
    print("creating hypertable")
    timescaledb.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
