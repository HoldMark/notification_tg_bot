from handlers.remove import remove_msgs_today
from schedule import set_schedule_for_today


async def reset_msgs_today(*args, **kwargs):
    await remove_msgs_today()
    set_schedule_for_today()
