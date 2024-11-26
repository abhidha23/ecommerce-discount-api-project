from sqlalchemy import (Column, 
    String, 
    Integer, 
    Float, 
    ForeignKey,
    Boolean, 
    DateTime, 
    ARRAY,
    Enum, 
    JSON)
from app.database import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.models.coupon import Coupon

class CouponDiscountDetails(Base):
    __tablename__ = "coupon_discount_details"

    id = Column(Integer, autoincrement=True)
    coupon_id = Column(UUID(as_uuid=True),ForeignKey(Coupon.id), primary_key=True, nullable=False)
    min_cart_amount = Column(Float, nullable=True) 
    min_quantity = Column(Integer, nullable=True) 
    discount_percentage = Column(Float, nullable=True)  
    discount_fixed = Column(Float, nullable=True) 
    applicable_product_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=True)  
    buy_product_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=True) 
    get_product_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=True)  
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)