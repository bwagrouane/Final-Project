from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from ..models.orders import OrderStatus


class OrderItemCreate(BaseModel):
    item_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderUpdate(BaseModel):
    cost: Optional[Decimal] = None
    status: Optional[OrderStatus] = None


class Order(BaseModel):
    id: int
    order_date: datetime
    cost: Decimal
    status: OrderStatus

    model_config = {
        "from_attributes": True
    }