from aiogram import Dispatcher

from aiogram.filters import Command
from handlers.mirror import mirror_answer
from handlers.remove import remove_msgs_today
from handlers.reset import reset_msgs_today


dp = Dispatcher()

dp.message.register(reset_msgs_today, Command('reset_today'))
dp.message.register(remove_msgs_today, Command('remove_today'))
dp.message.register(mirror_answer)
