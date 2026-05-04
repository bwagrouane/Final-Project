from sqlalchemy.orm import Session

from ..models.payments import Payment
from ..models.orders import Order


def create(db: Session, payment):
    db_order = db.query(Order).filter(Order.id == payment.order_id).first()
    if db_order is None:
        return None

    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
