from bot_init import bot
from time_message import auto_send_msg
from rand_time import schedule

from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def set_schedule_for_today():
    for i in schedule:
        scheduler.add_job(auto_send_msg, trigger='date', run_date=i, kwargs={'bot': bot})


scheduler.add_job(set_schedule_for_today, trigger='cron', day_of_week='mon-fri', hour=8)
