from sqlalchemy import Column, Integer, DECIMAL, DATETIME, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
import enum


class OrderStatus(str, enum.Enum):
    received = "received"
    packaging = "packaging"
    delivering = "delivering"
    delivered = "delivered"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, nullable=False, default=datetime.now)
    cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    status = Column(
        Enum(OrderStatus),
        nullable=False,
        default=OrderStatus.received
    )

    order_details = relationship("OrderDetail", back_populates="order")
    payment = relationship("Payment", back_populates="order", cascade="all, delete-orphan", uselist=False)