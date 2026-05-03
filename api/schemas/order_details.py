from typing import Optional
from pydantic import BaseModel
from .items import Item


class OrderDetailBase(BaseModel):
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    item_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item_id: int
    item: Item = None

    model_config = {
        "from_attributes": True
    }