from fastapi import APIRouter
from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.db.session import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session


router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return {"id": event_id}


@router.post("/", response_model=EventModel)
def create_event(payload: EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print("dataaaaa", data)
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    data = payload.model_dump()
    return {"id": event_id, **data}
