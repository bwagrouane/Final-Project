from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    discountMultiplier: str
    numberofUses: float


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    discountMultiplier: Optional[str] = None
    numberofUses: Optional[float] = None


class Promotion(PromotionBase):
    promoCode: int

    class ConfigDict:
        from_attributes = True
