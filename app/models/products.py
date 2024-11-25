from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy import JSON
from datetime import datetime
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, nullable=False)
