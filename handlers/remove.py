from aiogram import Bot
from aiogram.types import Message
from utils.remove_job import remove_job


async def remove_msgs_today(msg: Message, bot: Bot):

    user_id = msg.from_user.id
    remove_job(user_id)

    await bot.send_message(user_id, text='Убрали уведомления на сегодня')
