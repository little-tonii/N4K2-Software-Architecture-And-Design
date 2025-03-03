from datetime import datetime
from pydantic import BaseModel


class CustomerRegisterResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
