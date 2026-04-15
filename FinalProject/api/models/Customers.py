from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    email = Column(String(100), unique = True, Index=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    
    address = Column(String(255), nullable=False)
