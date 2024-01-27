from core.bot_init import bot
from utils.auto_send_msg import auto_send_msg
from utils.get_schedule import get_schedule_for_period
from core.config import TG_USER_ID

from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def set_schedule_for_today(user_id):

    schedule = get_schedule_for_period(amount=8, interval=5, start=9, end=18)

    for date_time in schedule:
        scheduler.add_job(auto_send_msg, trigger='date', run_date=date_time, kwargs={'bot': bot, 'user_id': user_id})


scheduler.add_job(set_schedule_for_today, trigger='cron', day_of_week='mon-fri', hour=8, kwargs={'user_id': TG_USER_ID})
