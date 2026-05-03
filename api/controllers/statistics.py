from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.order_details import OrderDetail
from ..models.orders import Order


def read_total_items_sold(db: Session):
    total = db.query(func.sum(OrderDetail.quantity)).scalar()

    if total is None:
        total = 0

    return {"total_items_sold": total}


def read_items_sold_by_day(db: Session, order_date):
    total = (
        db.query(func.sum(OrderDetail.quantity))
        .join(Order)
        .filter(func.date(Order.order_date) == order_date)
        .scalar()
    )

    if total is None:
        total = 0

    return {"date": order_date, "items_sold": total}