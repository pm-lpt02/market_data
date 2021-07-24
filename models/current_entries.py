from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from databases import Base


class CurrentEntry(Base):
    __tablename__ = 'current_entries'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    symbol_id = Column(Integer, nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    prev_close = Column(Float, nullable=True)
    open = Column(Float, nullable=True)
    bid = Column(String, nullable=False)
    ask = Column(String, nullable=False)
    day_range = Column(String, nullable=False)
    range_52wk = Column(String, nullable=False)
    volume = Column(Integer, nullable=False)
    avg_volume = Column(Integer, nullable=False)
    marketcap = Column(String, nullable=False)
    pe_ratio = Column(Float, nullable=True)
    eps = Column(Float, nullable=True)

