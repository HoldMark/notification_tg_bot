import logging

from aiogram import Bot
from aiogram.types import Message
from schedule import scheduler

logger = logging.getLogger(f'bot.{__name__}')


async def get_notification_list(msg: Message, bot: Bot):

    logger.info('Get List Command')

    user_id = msg.from_user.id
    job_list = scheduler.get_jobs()
    schedule = [job.next_run_time for job in job_list if job.name == 'auto_send_msg' and job.kwargs['user_id'] == user_id]
    text = ''

    if schedule:
        text = ''.join([str(i) + '\n' for i in schedule])
    else:
        text = 'Нет уведомлений на сегодня'

    try:
        await bot.send_message(user_id, text=text)
    except Exception as e:
        logger.error(f'Failed to send notification\'s list to user with id: {user_id}', exc_info=True)
