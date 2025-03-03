from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from .apis import customer_api
from .configs.exception_handler import global_exception_handler, http_exception_handler, validation_exception_handler

app = FastAPI(
    title="Django Ecommerce"
)

origins = [
    "*"
]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(customer_api.router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)