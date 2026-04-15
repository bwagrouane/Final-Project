from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotion"

    promoCode = Column(Integer, primary_key=True, index=True, autoincrement=True)
    discountMultiplier = Column(String(100), unique=True, nullable=True)
    numberofUses = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    
