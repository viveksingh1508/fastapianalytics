from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema
from api.db.config import DATABASE_URL

router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}]}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}
