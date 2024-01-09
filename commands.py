from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало работы'),
        BotCommand(command='remove_today', description='Не отправлять сегодня уведомления'),
        BotCommand(command='reset_today', description='Переустановить уведомления')
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
