from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True) # Primary key tracking what number review this is out of all reviews
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False) # ID to connect the review to users account
    user_name = Column(String, nullable=False) # Name (First, Last) of user
    rating = Column(Integer, nullable=False) # How many stars out of 5
    review = Column(String, nullable=True)  # User written review

    # customer = relationship("Customer", back_populates="reviews")