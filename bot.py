import asyncio
from aiogram import Dispatcher

from bot_init import bot
from logger import logger
from handlers import router
from schedule import scheduler


dp = Dispatcher()
dp.include_router(router)


async def main() -> None:

    logger.info('Start bot')
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
