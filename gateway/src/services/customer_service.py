from fastapi import Response

from typing import Annotated
from fastapi import Depends, HTTPException
import httpx
from passlib.context import CryptContext
from starlette import status

from ..schemas.response.customer_schema_response import CustomerRegisterResponse

from ..configs.variables import CUSTOMER_SERVICE_URL

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CustomerService:
    
    @staticmethod
    async def register_customer(email: str, password: str) -> CustomerRegisterResponse:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{CUSTOMER_SERVICE_URL}/email/{email}")
            if response.status_code == status.HTTP_200_OK:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email đã được sử dụng"
                )
            if response.status_code != status.HTTP_404_NOT_FOUND:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Có lỗi xảy ra với customer service"
                ) 
            hashed_password = bcrypt_context.hash(password)
            response = await client.post(
                f"{CUSTOMER_SERVICE_URL}/create",
                json={"email": email, "hashed_password": hashed_password}
            )
            if response.status_code != status.HTTP_201_CREATED:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=response.json().get("detail", "Lỗi từ Customer Service")
                )
            return CustomerRegisterResponse(
                id=response.json().get("id"),
                email=response.json().get("email"),
                created_at=response.json().get("created_at"),
                updated_at=response.json().get("updated_at")
            )