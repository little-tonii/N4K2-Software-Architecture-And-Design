from fastapi import HTTPException
from .schemas import CreateCustomerResponse, GetCustomerResponse, UpdateCustomerResponse
from sqlalchemy.orm import Session
from .models import Customer

def create_customer_task(session: Session, email: str, hashed_password: str) -> CreateCustomerResponse:
    new_customer = Customer(
        email=email,
        hashed_password=hashed_password
    )
    session.add(new_customer)
    session.commit()
    session.refresh(new_customer)
    return CreateCustomerResponse(
        id=new_customer.id,
        email=new_customer.email,
        created_at=new_customer.created_at,
        updated_at=new_customer.updated_at
    )

def get_customer_by_id_task(session: Session, customer_id: int) -> GetCustomerResponse:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return GetCustomerResponse(
        id=customer.id,
        email=customer.email,
        phone_number=customer.phone_number,
        address=customer.address,
        created_at=customer.created_at,
        updated_at=customer.updated_at
    )

def delete_customer_task(session: Session, customer_id: int) -> None:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    session.delete(customer)
    session.commit()
    
def update_customer_task(session: Session, customer_id: int, phone_number: str | None, hashed_password: str | None, address: str | None) -> UpdateCustomerResponse:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    customer.phone_number = phone_number or customer.phone_number
    customer.address = address or customer.address
    customer.hashed_password = hashed_password or customer.hashed_password
    session.commit()
    session.refresh(customer)
    return UpdateCustomerResponse(
        id=customer.id,
        email=customer.email,
        phone_number=customer.phone_number,
        address=customer.address,
        created_at=customer.created_at,
        updated_at=customer.updated_at
    )
    
def get_customer_by_email_task(session: Session, email: str) -> GetCustomerResponse:
    customer = session.query(Customer).filter(Customer.email == email).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Khách hàng không tồn tại")
    return GetCustomerResponse(
        id=customer.id,
        email=customer.email,
        phone_number=customer.phone_number,
        address=customer.address,
        created_at=customer.created_at,
        updated_at=customer.updated_at
    )