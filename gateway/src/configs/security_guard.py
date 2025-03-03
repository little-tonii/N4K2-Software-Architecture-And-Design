# from datetime import datetime, timezone
# from typing import Annotated
# from fastapi import Depends
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from fastapi import HTTPException
# from starlette import status
# from configs.variables import HASH_ALGORITHM, SECRET_KEY
# from utils.token_util import TokenKey

# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/login')        

# class TokenClaims:
#     id: int
    
#     def __init__(self, id: str):
#         self.id = id

# async def verify_access_token(
#         user_service: Annotated[UserService, Depends()],
#         token: Annotated[OAuth2PasswordBearer, Depends(oauth2_bearer)]) -> TokenClaims:
#     try:
#         payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[HASH_ALGORITHM])
#         user_id: int = payload.get(TokenKey.ID)
#         expires: int = payload.get(TokenKey.EXPIRES)
#         if user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
#         if expires and datetime.now(timezone.utc).timestamp() > expires:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
#         if user_service.find_user_by_id(id=user_id) is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')    
#         return TokenClaims(id=user_id)
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
    
# def verify_refresh_token(refresh_token: str) -> TokenClaims:
#     try:
#         payload = jwt.decode(token=refresh_token, key=SECRET_KEY, algorithms=[HASH_ALGORITHM])
#         user_id: int = payload.get(TokenKey.ID)
#         expires: int = payload.get(TokenKey.EXPIRES)
#         if user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
#         if expires and datetime.now(timezone.utc).timestamp() > expires:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
#         return TokenClaims(id=user_id)
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')