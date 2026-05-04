from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from .items import Item


class CartItemCreate(BaseModel):
    item_id: int
    quantity: int


class CartItemUpdate(BaseModel):
    quantity: int


class CartItem(BaseModel):
    id: int
    cart_id: int
    item_id: int
    quantity: int
    item: Optional[Item] = None

    model_config = {"from_attributes": True}


class CartCreate(BaseModel):
    items: list[CartItemCreate]


class Cart(BaseModel):
    id: int
    created_at: datetime
    cost: Decimal
    cart_items: list[CartItem] = []

    model_config = {"from_attributes": True}
