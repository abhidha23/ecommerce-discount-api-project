from pydantic import BaseModel
from typing import Dict, Optional
import uuid
from datetime import date


class CouponCreateSchema(BaseModel):
    type: str
    discount_details: Dict
    valid_from: str  
    valid_to: str    
    is_active: bool = True


class CouponResponse(BaseModel):
  type: str
  valid_from: date
  created_at:date
  valid_to: date
  id: uuid.UUID
  discount_details: Dict
  is_active: bool
  updated_at:Optional[date] = None
