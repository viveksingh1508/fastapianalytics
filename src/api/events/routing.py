from fastapi import APIRouter
from .models import (
    EventModel,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema,
    get_utc_now,
)
from api.db.session import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session, select


router = APIRouter()


@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)) -> EventListSchema:
    query = select(EventModel)
    results = session.exec(query).all()
    return {"results": results, "count": len(results)}


@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        return {"error": "Event not found"}
    return result


@router.post("/", response_model=EventModel)
def create_event(payload: EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.put("/{event_id}", response_model=EventModel)
def update_event(
    event_id: int, payload: EventUpdateSchema, session: Session = Depends(get_session)
):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        return {"error": "Event not found"}
    result.description = payload.description
    result.updated_at = get_utc_now()
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


@router.delete("/{event_id}", response_model=EventModel)
def delete_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        return {"error": "Event not found"}
    session.delete(result)
    session.commit()
    return result
