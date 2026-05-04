from decimal import Decimal
from sqlalchemy.orm import Session
from fastapi import Response, status

from ..models.cart import Cart, CartItem
from ..models.items import Item


def _recalculate_cost(db: Session, cart_id: int):
    cart_items = db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
    total = sum(
        (db.query(Item).filter(Item.id == ci.item_id).first().price * ci.quantity)
        for ci in cart_items
    )
    db.query(Cart).filter(Cart.id == cart_id).update({"cost": Decimal(str(total))})


def create(db: Session, cart):
    db_cart = Cart(cost=Decimal("0.00"))
    db.add(db_cart)
    db.flush()

    for ci in cart.items:
        db.add(CartItem(cart_id=db_cart.id, item_id=ci.item_id, quantity=ci.quantity))

    db.flush()
    _recalculate_cost(db, db_cart.id)
    db.commit()
    db.refresh(db_cart)
    return db_cart


def read_all(db: Session):
    return db.query(Cart).all()


def read_one(db: Session, cart_id: int):
    return db.query(Cart).filter(Cart.id == cart_id).first()

def read_one_item(db: Session, cart_item_id: int):
    return db.query(CartItem).filter(CartItem.id == cart_item_id).first()


def update(db: Session, cart_item_id: int, data):
    db_cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if db_cart_item is None:
        return None

    db_cart_item.quantity = data.quantity
    db.flush()
    _recalculate_cost(db, db_cart_item.cart_id)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def delete(db: Session, cart_item_id: int):
    db_cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if db_cart_item is None:
        return None

    cart_id = db_cart_item.cart_id
    db.delete(db_cart_item)
    db.flush()
    _recalculate_cost(db, cart_id)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
