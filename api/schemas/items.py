from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    quantity: int
    price: float


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None


class Item(ItemBase):
    id: int

    model_config = {
        "from_attributes": True
    }