from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from models.historic_entries import Historic_Entry
from schemas.historicSchema import HistoricView, HistoricDetail


def get_all(db: Session):
    entries = db.query(Historic_Entry).all()
    return entries


def get_past_entries(id: int, db: Session):
    entries = db.query(Historic_Entry).filter(Historic_Entry.symbol_id == id).all()
    return entries


