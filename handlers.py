from aiogram import Router, Bot
from aiogram.types import Message

router = Router()


@router.message()
async def mirror_answer(msg: Message, bot: Bot):
    await bot.send_message(msg.from_user.id, msg.text)
