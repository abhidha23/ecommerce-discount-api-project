from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from app.models.cart import Cart
from app.models.products import Products
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CartProductMapping(Base):
    __tablename__ = 'cart_product_mapping'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    cart_id = Column(UUID(as_uuid=True), ForeignKey(Cart.cart_id), nullable=False) 
    product_id = Column(UUID(as_uuid=True), ForeignKey(Products.product_id), nullable=False) 
    created_at =  Column(DateTime, nullable=False)
