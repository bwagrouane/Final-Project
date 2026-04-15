from pydantic import BaseModel


class ReviewBase(BaseModel):
    customer_id: int
    user_name: str
    rating: int
    review: str | None = None


class ReviewCreate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    review_id: int

    class Config:
        from_attributes = True