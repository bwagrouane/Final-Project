from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from ..dependencies.database import Base

class PaymentMethod(str, enum.Enum):
    cash = "cash"
    credit_card = "credit_card"
    online = "online"

class PaymentStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"
    refunded = "refunded"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    
  
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DATETIME, nullable=False, default=datetime.now)
    
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.pending)
    
    transaction_reference = Column(String(255), nullable=True)

    order = relationship("Order", back_populates="payment")
