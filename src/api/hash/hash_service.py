import bcrypt


class HashService:

    @classmethod
    async def hashed_password(cls, password: str) -> bytes:
        hashed_password = bcrypt.hashpw(
            password=password.encode("utf-8"), salt=bcrypt.gensalt()
        )
        return hashed_password

    @classmethod
    async def verify_password(
        cls, password: str, hashed_password: bytes
    ) -> bool:  # noqa
        return bcrypt.checkpw(
            password=password.encode("utf-8"), hashed_password=hashed_password
        )
