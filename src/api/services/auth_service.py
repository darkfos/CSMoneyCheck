import datetime
from src.api.auth.auth_service import AuthService
from src.api.dto.auth_dto import AuthUserData, AuthModel
from src.api.hash.hash_service import HashService
from src.api.dep import InterfaceUnitOfWork
from src.enums_cs import UserTypeEnum
from src.api.exceptions import UserException
from src.other import generate_random_key
from src.other.rabbit_service.producers.email_producer import send_email


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
                        type_token="access",  # noqa
                    )  # noqa
                    refresh_token = await AuthService.create_token(
                        data={"sub": str(user_info[0].get("id"))},
                        type_token="refresh",  # noqa
                    )  # noqa
                    return AuthModel(
                        access_token=token, refresh_token=refresh_token
                    )  # noqa
            await UserException.no_acceptable_password()

    @classmethod
    async def update_password_send_email(
        cls, uow: InterfaceUnitOfWork, token_data: dict, new_password: str
    ) -> None:
        """
        Send email message for confirm update
        :param token_data:
        :param new_password:
        :return:
        """

        async with uow:
            generate_key = await generate_random_key()
            is_upd_password = await uow.user_repository.update_user_secret_key(
                id_model=int(token_data.get("sub")), key=generate_key
            )
            user_data = await uow.user_repository.get_one(
                id_model=int(token_data.get("sub"))
            )
            if is_upd_password:
                await send_email(
                    data={
                        "email": user_data.get("email"),
                        "secret_key": generate_key,
                        "new_password": new_password,
                    }
                )  # noqa
                return None

    @classmethod
    async def update_password(
        cls, uow: InterfaceUnitOfWork, secret: str, new_password: str
    ) -> None:
        """
        Обновление пароля
        :param uow:
        :param secret:
        :param new_password:
        """

        async with uow:
            user_data = await uow.user_repository.find_by_secret(secret=secret)
            if user_data:
                upd_secret_key = (
                    await uow.user_repository.update_user_secret_key(  # noqa
                        id_model=user_data[0].get("id"), key=""
                    )
                )
                if upd_secret_key:
                    new_hashed_password = await HashService.hashed_password(
                        password=new_password
                    )  # noqa
                    upd_password = await uow.user_repository.update_data(
                        id_model=user_data[0].get("id"),
                        data_to_update={"hashed_password": new_hashed_password},  # noqa
                    )
                    if upd_password:
                        return None
            await UserException.no_update_user_password()

    @classmethod
    async def update_username(
        cls, uow: InterfaceUnitOfWork, new_username: str, token_data: dict
    ) -> None:  # noqa
        """
        User Service - Update username
        :param uow:
        :param new_username:
        :param token_data:
        """

        async with uow:
            is_upd = await uow.user_repository.update_data(
                id_model=int(token_data.get("sub")),
                data_to_update={"username": new_username},
            )

            if is_upd:
                return
            await UserException.no_update_username()
