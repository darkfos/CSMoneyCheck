from src.api.dep import InterfaceUnitOfWork
from src.database.postgres.repository import (
    UserRepository,
    UserTypeRepository,
    ReviewsRepository,
)  # noqa
from src.database.postgres.db_worker import DBWorker


class UnitOfWork(InterfaceUnitOfWork):
    async def __aenter__(self):
        self.db = DBWorker()
        await self.db.create_connection()
        self.user_repository: UserRepository = UserRepository(
            session=self.db.pool
        )  # noqa
        self.user_type_repository: UserTypeRepository = UserTypeRepository(
            session=self.db.pool
        )  # noqa
        self.review_repository: ReviewsRepository = ReviewsRepository(
            session=self.db.pool
        )  # noqa

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.db.pool.close()
