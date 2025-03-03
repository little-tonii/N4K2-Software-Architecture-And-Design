from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from .schemas import CreateCustomerRequest, CreateCustomerResponse, GetCustomerResponse, UpdateCustomerRequest, UpdateCustomerResponse
from sqlalchemy.orm import Session
from .database import get_db
from .service import create_customer_task, delete_customer_task, get_customer_by_email_task, get_customer_by_id_task, update_customer_task

router = APIRouter(prefix="/customer", tags=["Customer"])

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=CreateCustomerResponse)
def create_customer(session: Annotated[Session, Depends(get_db)], request: CreateCustomerRequest):
    return create_customer_task(
        email=request.email, 
        hashed_password=request.hashed_password, 
        session=session)

@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=GetCustomerResponse)
def get_customer_by_id(session: Annotated[Session, Depends(get_db)], id: int):
     return get_customer_by_id_task(session, id)

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(session: Annotated[Session, Depends(get_db)], id: int):
    return delete_customer_task(session, id)

@router.patch("/update/{id}", status_code=status.HTTP_200_OK, response_model=UpdateCustomerResponse)
def update_customer(session: Annotated[Session, Depends(get_db)], id: int, request: UpdateCustomerRequest):
    return update_customer_task(
        session=session, 
        customer_id=id, 
        hashed_password=request.hashed_password, 
        phone_number=request.phone_number, 
        address=request.address)

@router.get("/email/{email}", status_code=status.HTTP_200_OK, response_model=GetCustomerResponse)
def get_customer_by_email(session: Annotated[Session, Depends(get_db)], email: str):
    return get_customer_by_email_task(session=session, email=email)