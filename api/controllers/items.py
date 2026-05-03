from sqlalchemy.orm import Session
from fastapi import status, Response

from ..models.items import Item


def create(db: Session, item):
    db_item = Item(
        name=item.name,
        quantity=item.quantity,
        price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def read_all(db: Session, min_price: float | None = None, max_price: float | None = None):
    query = db.query(Item)
    if min_price is not None:
        query = query.filter(Item.price >= min_price)
    if max_price is not None:
        query = query.filter(Item.price <= max_price)
    return query.all()


def read_one(db: Session, item_id):
    return db.query(Item).filter(Item.id == item_id).first()


def update(db: Session, item_id, item):
    db_item = db.query(Item).filter(Item.id == item_id)
    update_data = item.model_dump(exclude_unset=True)
    db_item.update(update_data, synchronize_session=False)
    db.commit()
    return db_item.first()


def delete(db: Session, item_id):
    db_item = db.query(Item).filter(Item.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)