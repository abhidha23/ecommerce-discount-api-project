from sqlalchemy import (Column, 
    String, 
    Integer, 
    Float, 
    Boolean, 
    Date, 
    Enum, 
    JSON)
from app.database import Base  
from enum import Enum as PyEnum
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CouponType(PyEnum):
    CART_WISE = "cart-wise"
    PRODUCT_WISE = "product-wise"
    BXGY = "BxGy"

class Coupon(Base):
    __tablename__ = "coupons" 

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    type = Column(Enum(CouponType), nullable=False)
    discount_details = Column(JSON, nullable=False)
    valid_from = Column(Date, nullable=False)
    valid_to = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)

