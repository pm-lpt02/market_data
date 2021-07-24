from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from coreSchema import CoreModel


class CurrentBase(CoreModel):
    prev_close: Optional[float]
    day_range: Optional[str]


class CurrentEntry(CurrentBase):
    class Config():
        orm_mode = True


class CurrentDetail(BaseModel):
    symbol_id: int
    date: datetime
    prev_close: float
    open: float
    bid: str
    ask: str
    day_range: str
    range_52wk: str
    volume: int
    avg_volume: int
    marketcap: str
    pe_ratio: float
    eps: float

    class Config():
        orm_mode = True


class CurrentView(CurrentBase):
    symbol_id: int
    date: datetime
    prev_close: float
    open: float
    day_range: str

    class Config():
        orm_mode = True
