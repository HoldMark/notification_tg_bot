import logging

from aiogram import Bot
from aiogram.types import Message
from src.utils.remove_job import remove_job

logger = logging.getLogger(f'bot.{__name__}')


async def remove_msgs_today(msg: Message, bot: Bot):

    logger.info('Remove Command')

    user_id = msg.from_user.id
    remove_job(user_id)

    try:
        await bot.send_message(user_id, text='Убрали уведомления на сегодня')
    except Exception as e:
        logger.error(f'Failed to send msg about removing notifications to user with id: {user_id}', exc_info=True)
