from src.api.dto.auth_dto import AuthUserData
from src.api.hash.hash_service import HashService
from asyncpg import Pool


class UserService:

    @classmethod
    async def create_new_user(
            cls,
            user_data: AuthUserData,
            pool: Pool
    ) -> bool:
        hashed_password: bytes = await HashService.hashed_password(password=user_data.password)
