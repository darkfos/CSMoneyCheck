from typing import Literal, Union
from datetime import timedelta, datetime, timezone
from fastapi import Request, Response

import jwt
from src.api.exceptions import UserException

from src.configs import AuthSettings


class AuthService:

    @classmethod
    async def create_token(cls, data: dict, type_token: Literal["access", "refresh"]) -> str:
        match type_token:
            case "access":
                data.update({"exp": (datetime.now(timezone.utc) + timedelta(minutes=AuthSettings.JWT_SECRET_LIVE))})
                access_token = jwt.encode(
                    data,
                    AuthSettings.JWT_SECRET_KEY,
                    algorithm=AuthSettings.JWT_ALGORITHM
                )
                return access_token
            case "refresh":
                data.update({"exp": (datetime.now(timezone.utc) + timedelta(days=AuthSettings.JWT_REFRESH_LIVE))})
                refresh_token = jwt.encode(
                    data,
                    AuthSettings.JWT_REFRESH_SECRET_KEY,
                    algorithm=AuthSettings.JWT_ALGORITHM
                )
                return refresh_token
            case _:
                raise jwt.PyJWTError("Не удалось создать токен")

    @classmethod
    async def decode_token(cls, token: str, type_token: Literal["access", "refresh"]) -> Union[dict, bool]:
        match type_token:
            case "access":
                try:
                    return jwt.decode(
                        token,
                        AuthSettings.JWT_SECRET_KEY,
                        algorithms=[AuthSettings.JWT_ALGORITHM]
                    )
                except jwt.DecodeError:
                    return False
                except jwt.ExpiredSignatureError:
                    return False
            case "refresh":
                try:
                    return jwt.decode(
                        token,
                        AuthSettings.JWT_REFRESH_SECRET_KEY,
                        algorithms=[AuthSettings.JWT_ALGORITHM]
                    )
                except jwt.DecodeError:
                    return False
                except jwt.ExpiredSignatureError:
                    return False
            case _:
                raise jwt.PyJWTError("Не удалось расшифровать токен")

    @classmethod
    async def verify_user(cls, req: Request, res: Response):
        cookies = req.cookies
        if "access_token" in cookies and "refresh_token" in cookies:
            print(cookies.get("access_token"))
            decode_access_token = await cls.decode_token(
                token=cookies.get("access_token"),
                type_token="access"
            )

            if decode_access_token:
                return True
            else:
                decode_refresh_token = await cls.decode_token(
                    token=cookies.get("refresh_token"),
                    type_token="refresh"
                )
                if decode_refresh_token:
                    new_access_token = await cls.create_token(
                        data=decode_refresh_token,
                        type_token="access"
                    )
                    res.cookies.set_cookie("access_token", new_access_token)
                    return True
                else:
                    await UserException.no_right_refresh_token()
        await UserException.no_auth_user()
