from aiogram import Bot
from aiogram.types import Message
from data.text import GREETING_TEXT


async def start_command(msg: Message, bot: Bot):
    user_id = msg.from_user.id
    await bot.send_message(user_id, text=GREETING_TEXT, disable_web_page_preview=True)
