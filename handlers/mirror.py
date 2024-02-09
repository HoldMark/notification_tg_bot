import logging

from aiogram import Bot
from aiogram.types import Message


logger = logging.getLogger(f'bot.{__name__}')


async def mirror_answer(msg: Message, bot: Bot):

    logger.info('Mirror answer')

    try:
        await bot.send_message(msg.from_user.id, msg.text)
    except Exception as e:
        logger.error(f'Failed to send mirror msg to user with id: {msg.from_user.id}', exc_info=True)