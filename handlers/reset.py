from aiogram import Bot
from aiogram.types import Message

from schedule import set_schedule_for_today
from utils.remove_job import remove_job


async def reset_msgs_today(msg: Message, bot: Bot):
    user_id = msg.from_user.id
    remove_job(user_id)
    set_schedule_for_today(user_id)

    await bot.send_message(msg.from_user.id, text='Переустановили уведомления на сегодня')
