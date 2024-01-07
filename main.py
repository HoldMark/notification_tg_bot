import asyncio
from aiogram import Dispatcher

from core.bot_init import bot
from core.logger import logger
from schedule import scheduler
from commands import set_commands
from handler import router

dp = Dispatcher()
dp.include_router(router)


async def start_bot() -> None:

    logger.info('Start bot')

    try:
        scheduler.start()
        await set_commands(bot)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.info(e)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
