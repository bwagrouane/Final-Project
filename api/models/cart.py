from sqlalchemy import Column, ForeignKey, Integer, DATETIME, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now)
    cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)

    cart_items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    cart = relationship("Cart", back_populates="cart_items")
    item = relationship("Item")
