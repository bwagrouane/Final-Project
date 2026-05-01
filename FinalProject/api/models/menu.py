from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    item = Column(String, primary_key=True, index=True, autoincrement=False)
    prices = Column(Float)
    ingredients = Column(String)
    calories = Column(Integer)
    category = Column(String)
    
