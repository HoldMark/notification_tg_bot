from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from schedule import scheduler

router = Router()


@router.message(Command('remove_today'))
async def remove_msgs_today(*args, **kwargs):
    job_list = scheduler.get_jobs()

    for i in job_list:
        if i.name == 'auto_send_msg':
            scheduler.remove_job(i.id)


@router.message()
async def mirror_answer(msg: Message, bot: Bot):
    await bot.send_message(msg.from_user.id, msg.text)
