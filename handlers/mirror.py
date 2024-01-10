from aiogram import Bot
from aiogram.types import Message


async def mirror_answer(msg: Message, bot: Bot):
    await bot.send_message(msg.from_user.id, msg.text)
