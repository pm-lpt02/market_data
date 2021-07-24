from typing import Optional
from pydantic import BaseModel
from .coreSchema import CoreModel
from datetime import datetime


class HistoricEntryBase(CoreModel):
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    adj_close: Optional[float]
    volume: Optional[int]


class HistoricEntry(HistoricEntryBase):
    class Config():
        orm_mode = True


class HistoricView(BaseModel):
    symbol_id: int
    date: datetime
    open: float
    close: float


class HistoricDetail(HistoricEntryBase):
    symbol_id: int
    date: datetime
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int

    class Config():
        orm_mode = True



