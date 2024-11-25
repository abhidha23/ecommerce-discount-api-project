from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy import JSON
from datetime import datetime
from database import Base  


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    products = Column(JSON, nullable=False) 
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
