from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
   
    db_order = db.query(Order).filter(Order.id == payment.order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
        
    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
