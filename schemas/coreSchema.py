from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CoreModel(BaseModel):
    symbol_id: int
    date: Optional[datetime]
    open: Optional[float]
    volume: Optional[int]

