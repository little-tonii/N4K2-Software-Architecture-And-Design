from fastapi import APIRouter


router = APIRouter(prefix="/customer", tags=["Customer"])

async def create_category()