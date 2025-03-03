from sqlalchemy import Column, DateTime, Integer, String, func
from .database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email: str = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(255), nullable=False)
    refresh_token: str = Column(String(255), nullable=True)
    phone_number: str = Column(String(20), nullable=True)
    address: str = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)