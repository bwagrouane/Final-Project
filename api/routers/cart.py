from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schemas import cart as schemas
from ..controllers import cart
from ..dependencies.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Cart)
def create_cart(cart_data: schemas.CartCreate, db: Session = Depends(get_db)):
    return cart.create(db=db, cart=cart_data)


@router.get("/", response_model=list[schemas.Cart])
def read_carts(db: Session = Depends(get_db)):
    return cart.read_all(db)


@router.get("/{cart_id}", response_model=schemas.Cart)
def read_one_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = cart.read_one(db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return db_cart


@router.put("/items/{cart_item_id}", response_model=schemas.CartItem)
def update_cart_item(cart_item_id: int, data: schemas.CartItemUpdate, db: Session = Depends(get_db)):
    db_item = cart.update(db=db, cart_item_id=cart_item_id, data=data)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return db_item


@router.delete("/items/{cart_item_id}")
def delete_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    db_item = cart.read_one_item(db, cart_item_id=cart_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return cart.delete(db=db, cart_item_id=cart_item_id)
