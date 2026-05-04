from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class ReviewBase(BaseModel):
    userid: int
    username: Optional[str] = None
    rating: Optional[Decimal] = None
    review: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    userid: Optional[int] = None
    username: Optional[str] = None
    rating: Optional[Decimal] = None
    review: Optional[str] = None


class Review(BaseModel):
    id: int
    userid: int
    username: Optional[str] = None
    rating: Optional[Decimal] = None
    review: Optional[str] = None

    class ConfigDict:
        from_attributes = True
