from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало работы'),
        BotCommand(command='set_today', description='Установить список уведомлений'),
        BotCommand(command='remove_today', description='Не отправлять сегодня уведомления'),
        BotCommand(command='reset_today', description='Переустановить уведомления'),
        BotCommand(command='get_list', description='Получить список уведомлений'),
        BotCommand(command='prolong', description='Продлить на n часов')
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
