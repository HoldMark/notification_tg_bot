import logging

import asyncio
from core.bot_init import bot
from core.dispetcher import dp

from core.schedule import scheduler
from core.commands import set_commands


logger = logging.getLogger(f'bot.{__name__}')


async def start_bot() -> None:
    logger.info('Start bot')

    try:
        scheduler.start()
        await set_commands(bot)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error('Error in start', exc_info=True)
    finally:
        logger.info('Stop bot')
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
