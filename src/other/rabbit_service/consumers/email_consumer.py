from aio_pika.message import IncomingMessage
from src.other.rabbit_service.rabbit_service import (
    RabbitMQService,
    AbstractRobustConnection,
)  # noqa
from src.other.email_service.email_worker import EmailWorker
import asyncio
import json


async def email_consumer() -> None:
    """
    Consumer for proccess data in email queue
    """

    connection: AbstractRobustConnection = await RabbitMQService.connect()  # noqa

    async with connection.channel() as ch:
        queue = await ch.declare_queue(name="email", durable=True)
        await ch.set_qos(prefetch_count=1)
        while True:
            await queue.consume(proccess_email_messages)


async def proccess_email_messages(message: IncomingMessage):
    async with message.process() as ms:
        # Отправка сообщения по почте
        message_from_queue = ms.body.decode("utf-8")
        message_from_queue = message_from_queue.replace("'", '"')
        message_from_queue = json.loads(message_from_queue)
        EmailWorker.send_message(
            url_update="http://127.0.0.1:8000/api/v1/auth/approve_upd_password?secret={}&new_password={}".format(  # noqa
                message_from_queue.get("secret_key"),
                message_from_queue.get("new_password"),
            ),
            email_user=message_from_queue.get("email"),
        )


if __name__ == "__main__":
    asyncio.run(email_consumer())
