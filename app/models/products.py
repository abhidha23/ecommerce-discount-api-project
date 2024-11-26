from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy import JSON
from datetime import datetime
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    product_name = Column(String(100), nullable=False)
    product_price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
