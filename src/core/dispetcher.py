from aiogram import Dispatcher
from aiogram.filters import Command

from src.handlers.prolong import prolong, get_hours
from src.handlers.start import start_command
from src.handlers.mirror import mirror_answer
from src.handlers.reset import reset_msgs_today
from src.handlers.set_today import set_ntf_today
from src.handlers.remove import remove_msgs_today
from src.handlers.get_list import get_notification_list
from src.utils.states_prolong import ProlongState


dp = Dispatcher()

dp.message.register(start_command, Command('start'))
dp.message.register(get_notification_list, Command('get_list'))
dp.message.register(set_ntf_today, Command('set'))
dp.message.register(reset_msgs_today, Command('reset'))
dp.message.register(remove_msgs_today, Command('remove'))
dp.message.register(prolong, Command('prolong'))
dp.message.register(get_hours, ProlongState.GET_HOUR)

dp.message.register(mirror_answer)
