from aio_pika import connect_robust
from aio_pika.robust_connection import AbstractRobustConnection  # noqa
from src.configs.db_settings import DatabaseSettings


class RabbitMQService:

    @classmethod
    async def connect(cls) -> AbstractRobustConnection:
        cls.connection: AbstractRobustConnection = await connect_robust(
            f"amqp://guest:guest@{DatabaseSettings.RABBIT_MQ_URI}/"  # noqa
        )

        return cls.connection
