import datetime
from src.api.dto.auth_dto import AuthUserData
from src.api.hash.hash_service import HashService
from src.api.dep import InterfaceUnitOfWork
from src.enums_cs import UserTypeEnum
from src.api.exceptions import UserException


class UserService:

    @classmethod
    async def create_new_user(
        cls, user_data: AuthUserData, uow: InterfaceUnitOfWork
    ) -> bool:
        hashed_password: bytes = await HashService.hashed_password(
            password=user_data.password
        )
        async with uow:
            data_to_add: tuple = (
                UserTypeEnum.USER.value,
                user_data.email,
                hashed_password,
                "",
                datetime.date.today(),
            )
            req = await uow.user_repository.add_data(data=data_to_add)

            if req:
                return
            print(req)
            await UserException.no_register_user()
