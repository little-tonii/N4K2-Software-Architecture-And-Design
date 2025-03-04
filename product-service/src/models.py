from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ObjectId không hợp lệ")
        return str(v)
    
class Category(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str

    class Config:
        json_encoders = {ObjectId: str}
    
class Product(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    description: Optional[str] = None
    price: float
    category_ids: List[str] = []

    class Config:
        json_encoders = {ObjectId: str}