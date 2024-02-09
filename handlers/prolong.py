import logging

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states_prolong import ProlongState

from utils.remove_job import remove_job
from schedule import set_schedule_for_period


logger = logging.getLogger(f'bot.{__name__}')


async def prolong(msg: Message, bot: Bot, state: FSMContext):

    logger.info('Prolong Command')

    try:
        await bot.send_message(msg.from_user.id, text='Укажите кол-во часов в диапазоне от 1 до 5, на которое необходимо продлить отправку уведомлений.\n\nЧтобы отменить установку отправьте /exit')
    except Exception as e:
        logger.error('Failed to send msg with instructions for prolongation')

    await state.set_state(ProlongState.GET_HOUR)


# TODO нужна проверка на установку, чтобы не смешивалось с основными уведомлениями

async def get_hours(msg: Message, bot: Bot, state: FSMContext):

    user_id = msg.from_user.id

    if msg.text == '/exit':

        logger.info('Exit from prolongation state')
        await state.clear()

    else:

        hours = msg.text

        try:
            hours = int(hours)
        except ValueError as e:
            await bot.send_message(user_id, text='Укажите число')
        else:
            if hours <= 0:
                await bot.send_message(user_id, text='Укажите число больше 0')
            elif hours > 5:
                await bot.send_message(user_id, text='Укажите число меньше 6')
            else:

                logger.info('Remove job to set new jobs for prolongation')
                remove_job(user_id)

                logger.info('Set schedule for prolongation')
                set_schedule_for_period(user_id, hours)

                await bot.send_message(user_id, text=f'Продлили уведомления на {hours} ч.')
                await state.clear()
