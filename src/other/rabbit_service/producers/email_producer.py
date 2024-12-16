from src.other.rabbit_service.rabbit_service import (
    RabbitMQService,
    AbstractRobustConnection,
)  # noqa
from aio_pika.message import Message
from typing import Dict


async def send_email(data: Dict[str, str]) -> None:
    """
    Producers for send message in email
    :param data:
    """

    connection: AbstractRobustConnection = await RabbitMQService.connect()

    async with connection.channel() as ch:
        queue = await ch.declare_queue("email", durable=True)
        await ch.default_exchange.publish(
            message=Message(body=str(data).encode()), routing_key=queue.name
        )
