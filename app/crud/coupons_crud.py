from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.create_coupons_schema import CouponCreateSchema
from app.models.coupon import Coupon


def create_coupon(db: Session, request:CouponCreateSchema):
    try:
        valid_from = datetime.strptime(request.valid_from, "%Y-%m-%d")
        valid_to = datetime.strptime(request.valid_to, "%Y-%m-%d")

        new_coupon = Coupon(
            type=request.type,
            discount_details=request.discount_details,
            valid_from=valid_from,
            valid_to=valid_to,
            created_at = datetime.utcnow(),
            is_active=request.is_active
        )
        db.add(new_coupon)
        db.commit()
        db.refresh(new_coupon)
        return new_coupon
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating coupon: {e}")