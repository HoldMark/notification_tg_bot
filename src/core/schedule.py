import logging


from src.core.bot_init import bot
from src.utils.auto_send_msg import auto_send_msg
from src.utils.get_schedule import get_schedule_for_period, get_schedule_for_hours
from src.core.config import TG_USER_ID

from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


logger = logging.getLogger(f'bot.{__name__}')


def set_schedule_for_today(user_id):

    logger.info('Set schedule for today')

    schedule = get_schedule_for_period(amount=8, interval=5, start=9, end=18)

    for date_time in schedule:
        scheduler.add_job(auto_send_msg, trigger='date', run_date=date_time, kwargs={'bot': bot, 'user_id': user_id})
        logger.debug(f'Today: Add job for user with id: {user_id} and with date_time: {date_time}')


def set_schedule_for_period(user_id, hours):

    logger.info('Set schedule for period')

    schedule = get_schedule_for_hours(hours)

    for date_time in schedule:
        scheduler.add_job(auto_send_msg, trigger='date', run_date=date_time, kwargs={'bot': bot, 'user_id': user_id})
        logger.debug(f'Period: Add job for user with id: {user_id} and with date_time: {date_time}')


scheduler.add_job(set_schedule_for_today, trigger='cron', day_of_week='mon-fri', hour=8, kwargs={'user_id': TG_USER_ID})
