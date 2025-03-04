from motor.motor_asyncio import AsyncIOMotorClient
from .database import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
database = client.items_db

product_collection = database.get_collection("products")
category_collection = database.get_collection("categories")