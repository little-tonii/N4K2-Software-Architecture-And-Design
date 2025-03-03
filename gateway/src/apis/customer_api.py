
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from ..schemas.response.customer_schema_response import CustomerLoginResponse, CustomerRegisterResponse

from ..schemas.requests.customer_schema_request import CustomerLoginRequest, CustomerRegisterRequest
from ..services.customer_service import CustomerService

router = APIRouter(prefix="/customer", tags=["Customer"])

@router.post(path="/register", status_code=status.HTTP_201_CREATED, response_model=CustomerRegisterResponse)
async def register(request: CustomerRegisterRequest):
    return await CustomerService.register_customer(email=request.email, password=request.password)

@router.post(path="/login", status_code=status.HTTP_200_OK, response_model=CustomerLoginResponse)
async def login(request: CustomerLoginRequest):
    return await CustomerService.login_customer(email=request.email, password=request.password)