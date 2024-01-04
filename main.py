import asyncio
from aiogram import Dispatcher

from core.bot_init import bot
from core.logger import logger
from schedule import scheduler


dp = Dispatcher()


async def main() -> None:

    logger.info('Start bot')
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
