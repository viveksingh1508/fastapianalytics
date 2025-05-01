from typing import List, Optional
from datetime import datetime
import sqlmodel
from sqlmodel import SQLModel, Field
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now


# def get_utc_now():
#     return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


class EventModel(TimescaleModel, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)

    page: str = Field(index=True)
    description: Optional[str] = ""

    # created_at: datetime = Field(
    #     default_factory=get_utc_now,
    #     sa_type=sqlmodel.DateTime(timezone=True),
    #     nullable=False,
    # )

    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False,
    )

    __chunk_time_interval__ = "INTERVAL 1 day"
    __drop__after__ = "INTERVAL 3 months"


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")


class EventUpdateSchema(SQLModel):
    description: str


class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int
