from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestFormStrict
from craft.schemas.user import DbUser

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestFormStrict, Depends()]):
    user = DbUser.find_one(DbUser.email == form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password")
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
