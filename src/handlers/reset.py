import logging

from aiogram import Bot
from aiogram.types import Message

from src.core.schedule import set_schedule_for_today
from src.utils.remove_job import remove_job

logger = logging.getLogger(f'bot.{__name__}')


async def reset_msgs_today(msg: Message, bot: Bot):

    logger.info('Reset Notification Command')

    user_id = msg.from_user.id
    remove_job(user_id)
    set_schedule_for_today(user_id)

    try:
        await bot.send_message(msg.from_user.id, text='Переустановили уведомления на сегодня')
    except Exception as e:
        logger.error(f'Failed to send msg about resetting notifications to user with id: {user_id}', exc_info=True)
