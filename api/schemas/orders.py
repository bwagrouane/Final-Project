from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from ..models.orders import OrderStatus


class OrderBase(BaseModel):
    cost: Decimal


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    cost: Optional[Decimal] = None
    status: Optional[OrderStatus] = None


class Order(OrderBase):
    id: int
    order_date: datetime
    status: OrderStatus

    class ConfigDict:
        from_attributes = True
