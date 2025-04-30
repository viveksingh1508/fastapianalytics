import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise ValueError("DATABASE_URL is not set in the environment variables")
engine = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print("Database initialized")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
