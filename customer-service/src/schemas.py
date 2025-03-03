from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator
from email_validator import validate_email, EmailNotValidError

class ErrorResponse(BaseModel):
    message: str
    
class ErrorsResponse(BaseModel):
    messages: list[str]
    
class CreateCustomerRequest(BaseModel):
    email: str
    hashed_password: str
    
class CreateCustomerResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
    
class GetCustomerResponse(BaseModel):
    id: int
    email: str
    phone_number: str | None
    address: str | None
    created_at: datetime
    updated_at: datetime
    
class UpdateCustomerRequest(BaseModel):
    hashed_password: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class UpdateCustomerResponse(BaseModel):
    id: int
    email: str
    phone_number: str | None
    address: str | None
    created_at: datetime
    updated_at: datetime