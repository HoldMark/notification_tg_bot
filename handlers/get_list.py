from aiogram import Bot
from aiogram.types import Message
from schedule import scheduler


async def get_notification_list(msg: Message, bot: Bot):
    job_list = scheduler.get_jobs()
    schedule = [i.next_run_time for i in job_list if i.name == 'auto_send_msg']
    text = ''

    if schedule:
        text = ''.join([str(i) + '\n' for i in schedule])
    else:
        text = 'Нет уведомлений на сегодня'

    await bot.send_message(msg.from_user.id, text=text)
