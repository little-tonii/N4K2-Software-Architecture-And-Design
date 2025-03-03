import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY")
HASH_ALGORITHM: str = os.getenv("HASH_ALGORITHM")
ACCESS_TOKEN_EXPIRES: int = int(os.getenv("ACCESS_TOKEN_EXPIRES"))
REFRESH_TOKEN_EXPIRES: int = int(os.getenv("REFRESH_TOKEN_EXPIRES"))
CUSTOMER_SERVICE_URL = "http://customer_service:8000/customer"