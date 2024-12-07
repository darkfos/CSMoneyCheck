from fastapi.exceptions import HTTPException
from fastapi import status


class UserException:

    @classmethod
    async def no_register_user(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="No register new user"
        )
