from datetime import datetime
from pydantic import BaseModel


class CustomerRegisterResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

class CustomerLoginResponse(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str