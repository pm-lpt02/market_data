from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from databases import Base


class Historic_Entry(Base):
    __tablename__ = 'historic_entries'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    symbol_id = Column(Integer, nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    adj_close = Column(Float, nullable=True)
    volume = Column(Integer, nullable=True)


