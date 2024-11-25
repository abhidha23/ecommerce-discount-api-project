from pydantic import BaseModel
from typing import Dict

class CouponCreateSchema(BaseModel):
    type: str
    discount_details: Dict
    valid_from: str  
    valid_to: str    
    is_active: bool = True