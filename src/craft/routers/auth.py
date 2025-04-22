from typing import Annotated
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestFormStrict
from craft.auth.auth import authenticate_user, create_access_token
from craft.schemas.token import Token
from craft.config import CONFIG
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def get_token(
    form_data: Annotated[OAuth2PasswordRequestFormStrict, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=CONFIG.auth_token_expire)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
