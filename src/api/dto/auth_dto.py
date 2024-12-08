from pydantic import BaseModel, Field, EmailStr
from typing import Annotated


class AuthModel(BaseModel):
    access_token: Annotated[str, Field()]
    refresh_token: Annotated[str, Field()]


class AuthUserData(BaseModel):
    email: Annotated[EmailStr, Field()]
    password: Annotated[str, Field()]
