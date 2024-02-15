import logging

from aiogram import Bot
from aiogram.types import Message
from src.utils.get_text_data import TextData


logger = logging.getLogger(f'bot.{__name__}')


async def start_command(msg: Message, bot: Bot):

    logger.info('Start Command')
    user_id = msg.from_user.id

    try:
        await bot.send_message(user_id, text=TextData.greeting, disable_web_page_preview=True)
    except Exception as e:
        logger.error(f'Failed to send greeting message to user with id: {user_id}', exc_info=True)
