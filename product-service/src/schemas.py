from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    
class ErrorsResponse(BaseModel):
    messages: list[str]
    
class CreateCategoryRequest(BaseModel):
    name: str
    
class CreateCategoryResponse(BaseModel):
    id: str
    name: str
    
class CategoryResponse(BaseModel):
    id: str
    name: str
class GetAllCategoryResponse(BaseModel):
    categories: list[CategoryResponse]
    
class UpdateCategoryRequest(BaseModel):
    name: str
    
class UpdateCategoryResponse(BaseModel):
    id: str
    name: str