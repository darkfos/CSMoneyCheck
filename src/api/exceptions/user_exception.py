from fastapi.exceptions import HTTPException
from fastapi import status


class UserException:

    @classmethod
    async def no_register_user(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="No register new user"
        )

    @classmethod
    async def no_acceptable_password(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No acceptable password",  # noqa
        )

    @classmethod
    async def no_auth_user(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not unauthorized",  # noqa
        )

    @classmethod
    async def no_right_refresh_token(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No right refresh token",  # noqa
        )

    @classmethod
    async def no_update_user_password(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Не удалось обновить пароль",
        )
