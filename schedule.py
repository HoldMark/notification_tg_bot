from core.bot_init import bot
from utils.auto_send_msg import auto_send_msg
from utils.random_time_schedule import get_schedule_for_today

from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def set_schedule_for_today():

    schedule = get_schedule_for_today()

    for i in schedule:
        scheduler.add_job(auto_send_msg, trigger='date', run_date=i, kwargs={'bot': bot})


scheduler.add_job(set_schedule_for_today, trigger='cron', day_of_week='mon-fri', hour=8)
