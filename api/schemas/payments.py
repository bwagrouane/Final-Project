from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional

class PaymentBase(BaseModel):
    amount: Decimal
    payment_method: str
    order_id: int

class PaymentCreate(PaymentBase):
   pass

class PaymentResponse(PaymentBase):
    id: int
    payment_date: datetime
    status: str
    transaction_reference: Optional[str]

    model_config = ConfigDict(from_attributes=True)
