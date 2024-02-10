from aiogram.fsm.state import StatesGroup, State


class ProlongState(StatesGroup):
    GET_HOUR = State()
