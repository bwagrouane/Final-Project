from sqlalchemy.orm import Session
from ..models.reviews import Reviews
from ..schemas.reviews import ReviewCreate


def create_review(review: ReviewCreate, db: Session):
    new_review = Reviews(
        userid=review.userid,
        username=review.username,
        rating=review.rating,
        review=review.review
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


def get_all_reviews(db: Session):
    return db.query(Reviews).all()
