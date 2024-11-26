from fastapi import APIRouter, HTTPException, Query, Depends
from app.schemas.create_coupons_schema import CouponCreateSchema, CouponResponse
from app.crud.coupons_crud import create_coupon
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello World"}

@router.post("/coupons", response_model = CouponResponse)
async def create_coupon_service(request: CouponCreateSchema, db: Session = Depends(get_db)):
    try:
        new_coupon = create_coupon(db=db, request=request)
        return new_coupon
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating coupon: {e}")