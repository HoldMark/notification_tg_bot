from aiogram import Bot
from aiogram.types import Message
from schedule import set_schedule_for_today


async def set_ntf_today(msg: Message, bot: Bot):

    user_id = msg.from_user.id
    set_schedule_for_today(user_id)

    await bot.send_message(user_id, text='Установили на сегодня')
