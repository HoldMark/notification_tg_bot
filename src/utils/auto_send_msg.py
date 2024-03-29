from aiogram import Bot
from src.core.config import TG_USER_ID
from src.utils.random_text import get_random_text


async def auto_send_msg(bot: Bot, user_id=TG_USER_ID):
    await bot.send_message(user_id, text=get_random_text())
