from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False)

    order_details = relationship("OrderDetail", back_populates="item") 