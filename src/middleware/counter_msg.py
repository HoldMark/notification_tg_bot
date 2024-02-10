from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from aiogram.fsm.context import FSMContext


class CounterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.text in ['/start', '/get_list', '/set', '/reset', '/remove', '/prolong']:
            await event.answer(event.get('state'))
        return await handler(event, data)


# async def clear_state(event: Message) -> None:
#     state: FSMContext = event.get('state')
#
#     if state is not None:
#         await state.clear()
