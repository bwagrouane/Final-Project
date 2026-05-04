from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..schemas.reviews import Review, ReviewCreate
from ..controllers import reviews  # <-- matches your file name

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return reviews.create_review(review, db)


@router.get("/", response_model=list[Review])
def get_all_reviews(db: Session = Depends(get_db)):
    return reviews.get_all_reviews(db)
