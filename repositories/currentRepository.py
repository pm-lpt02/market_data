from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from models.current_entries import CurrentEntry
from schemas.currentSchema import CurrentView, CurrentDetail


def get_all(db: Session):
    entries = db.query(CurrentEntry).all()
    return entries


def get_past_entries(id: int, db: Session):
    entries = db.query(CurrentEntry).filter(CurrentEntry.symbol_id == id).all()
    return entries




