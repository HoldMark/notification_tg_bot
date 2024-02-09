import logging
import core.logger

import asyncio
from core.bot_init import bot
from core.dispetcher import dp

from schedule import scheduler
from commands import set_commands


logger = logging.getLogger(f'bot.{__name__}')


async def start_bot() -> None:
    logger.info('Start bot')
    logger.info(bot.token)

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
