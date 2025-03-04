from fastapi import APIRouter
from starlette import status

from .schemas import CreateCategoryRequest, CreateCategoryResponse, GetAllCategoryResponse, UpdateCategoryRequest, UpdateCategoryResponse
from .services import create_category_task, delete_category_task, get_all_category_task, update_category_task

router = APIRouter(prefix="/category", tags=["Category"])

@router.post(path="/create", status_code=status.HTTP_201_CREATED, response_model=CreateCategoryResponse)
async def create_category(request: CreateCategoryRequest):
    return await create_category_task(name=request.name)

@router.get(path="/", status_code=status.HTTP_200_OK, response_model=GetAllCategoryResponse)
async def get_all_category():
    return await get_all_category_task()

@router.post(path="/{id}", status_code=status.HTTP_200_OK, response_model=UpdateCategoryResponse)
async def update_category(request: UpdateCategoryRequest, id: str):
    return await update_category_task(id=id, name=request.name)

@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: str):
    await delete_category_task(id=id)