from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MenuBase(BaseModel):
    item: str
    prices: float
    ingredients: str
    calories: int
    category: str


class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    item: Optional[str] = None
    prices: Optional[float] = None
    ingredients: Optional[str] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class Menu(MenuBase):
    class ConfigDict:
        from_attributes = True
