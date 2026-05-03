from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from ..controllers import statistics
from ..dependencies.database import get_db

router = APIRouter()


@router.get("/items/total")
def read_total_items_sold(db: Session = Depends(get_db)):
    return statistics.read_total_items_sold(db)


@router.get("/items/day/{order_date}")
def read_items_sold_by_day(order_date: date, db: Session = Depends(get_db)):
    return statistics.read_items_sold_by_day(db, order_date=order_date)