from aiogram import Bot
from core.config import TG_USER_ID
from utils.random_text import get_random_text


async def auto_send_msg(bot: Bot):
    await bot.send_message(TG_USER_ID, text=get_random_text())
