from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/customer", tags=["Customer"])

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_customer():
    pass

@router.get("/{id}")
async def get_customer(id: int):
    pass

@router.delete("/{id}")
async def delete_customer(id: int):
    pass

@router.put("/update")
async def update_customer():
    pass