import datetime
from src.api.auth.auth_service import AuthService
from src.api.dto.auth_dto import AuthUserData, AuthModel
from src.api.hash.hash_service import HashService
from src.api.dep import InterfaceUnitOfWork
from src.configs import AuthSettings
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
            await UserException.no_register_user()

    @classmethod
    async def login_user(
        cls, uow: InterfaceUnitOfWork, user_data: AuthUserData
    ) -> AuthModel:
        async with uow:
            user_info = await uow.user_repository.find_by_email(
                email=user_data.email
            )  # noqa
            if user_info:
                verify_user = await HashService.verify_password(
                    password=user_data.password,
                    hashed_password=user_info[0].get("hashed_password"),
                )

                if verify_user:
                    # Create token
                    token = await AuthService.create_token(  # noqa
                        data={"sub": str(user_info[0].get("id"))},
                        type_token="access"
                    )  # noqa
                    refresh_token = await AuthService.create_token(
                            data={"sub": str(user_info[0].get("id"))},
                            type_token="refresh"
                        ) # noqa
                    return AuthModel(
                        access_token=token, refresh_token=refresh_token
                    )  # noqa
                await UserException.no_acceptable_password()
