from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userid = Column(Integer, nullable=False)
    username = Column(String(100), nullable=True)
    rating = Column(DECIMAL(3,2), nullable=True)
    review = Column(String(255), nullable=True)
