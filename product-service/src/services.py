from bson import ObjectId
from fastapi import HTTPException
from .schemas import CategoryResponse, CreateCategoryResponse, GetAllCategoryResponse, UpdateCategoryResponse
from .database import category_collection

async def update_category_task(id: str, name: str) -> UpdateCategoryResponse:
    update_result = await category_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name}}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Danh mục không tồn tại")
    return UpdateCategoryResponse(id=id, name=name)


async def create_category_task(name: str) -> CreateCategoryResponse:
    category_dict = {"name": name}
    result = await category_collection.insert_one(category_dict)
    return CreateCategoryResponse(id=str(result.inserted_id), name=name)

async def get_all_category_task() -> GetAllCategoryResponse:
    categories_cursor = category_collection.find()
    categories = await categories_cursor.to_list(length=None)
    return GetAllCategoryResponse(
        categories=[CategoryResponse(id=str(cat["_id"]), name=cat["name"]) for cat in categories]
    )
    
async def delete_category_task(id: str) -> None:
    delete_result = await category_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Danh mục không tồn tại")