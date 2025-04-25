from fastapi import APIRouter
from .models import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.db.config import DATABASE_URL

router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}


@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": 123, **data}


@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": event_id, **data}
