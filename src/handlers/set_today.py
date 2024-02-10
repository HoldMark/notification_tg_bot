import logging

from aiogram import Bot
from aiogram.types import Message
from src.core.schedule import set_schedule_for_today


logger = logging.getLogger(f'bot.{__name__}')


async def set_ntf_today(msg: Message, bot: Bot):

    logger.info('Set Notification Command')

    user_id = msg.from_user.id
    set_schedule_for_today(user_id)

    try:
        await bot.send_message(user_id, text='Установили на сегодня')
    except Exception as e:
        logger.error(f'Failed to send msg about setting notification to user with id: {user_id}', exc_info=True)
