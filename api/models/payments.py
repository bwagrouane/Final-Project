from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from ..dependencies.database import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DATETIME, default=datetime.now)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(50), default="pending")
