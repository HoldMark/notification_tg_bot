from aiogram import Dispatcher
from aiogram.filters import Command

from handlers.start import start_command
from handlers.mirror import mirror_answer
from handlers.reset import reset_msgs_today
from handlers.set_today import set_ntf_today
from handlers.remove import remove_msgs_today
from handlers.get_list import get_notification_list


dp = Dispatcher()

dp.message.register(start_command, Command('start'))
dp.message.register(get_notification_list, Command('get_list'))
dp.message.register(set_ntf_today, Command('set_today'))
dp.message.register(reset_msgs_today, Command('reset_today'))
dp.message.register(remove_msgs_today, Command('remove_today'))

dp.message.register(mirror_answer)
