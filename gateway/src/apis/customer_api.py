
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from ..configs.security_guard import TokenClaims, verify_access_token

from ..schemas.response.customer_schema_response import CustomerInforResponse, CustomerLoginResponse, CustomerRegisterResponse

from ..schemas.requests.customer_schema_request import CustomerRegisterRequest, CustomerUpdateInforRequest
from ..services.customer_service import CustomerService

router = APIRouter(prefix="/customer", tags=["Customer"])

@router.post(path="/register", status_code=status.HTTP_201_CREATED, response_model=CustomerRegisterResponse)
async def register(request: CustomerRegisterRequest):
    return await CustomerService.register_customer(email=request.email, password=request.password)

@router.post(path="/login", status_code=status.HTTP_200_OK, response_model=CustomerLoginResponse)
async def login(login_form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await CustomerService.login_customer(email=login_form.username, password=login_form.password)

@router.get(path="/infor", status_code=status.HTTP_200_OK, response_model=CustomerInforResponse)
async def infor(claims: Annotated[TokenClaims, Depends(verify_access_token)]):
    return await CustomerService.infor_customer(id=claims.id)

@router.patch(path="/update-infor", status_code=status.HTTP_200_OK, response_model=CustomerInforResponse)
async def update_infor(claims: Annotated[TokenClaims, Depends(verify_access_token)], request: CustomerUpdateInforRequest):
    return await CustomerService.update_customer_infor(id=claims.id, phone_number=request.phone_number, address=request.address)