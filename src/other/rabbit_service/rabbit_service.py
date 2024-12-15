from aio_pika import connect_robust
from aio_pika.robust_connection import AbstractRobustConnection  # noqa


class RabbitMQService:

    @classmethod
    async def connect(cls) -> AbstractRobustConnection:
        print("connect")
        cls.connection: AbstractRobustConnection = await connect_robust(
            "amqp://guest:guest@localhost/"
        )

        return cls.connection
