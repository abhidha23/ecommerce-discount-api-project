from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy import JSON
from datetime import datetime
from app.database import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Cart(Base):
    __tablename__ = 'cart'

    cart_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = Column(DateTime, nullable=False)
    cart_quantity = Column(Integer, default=0) 
    total_amount = Column(Float, default=0.0) 
