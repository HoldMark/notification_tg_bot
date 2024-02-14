from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable
from aiogram.fsm.context import FSMContext


class ClearStateMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data.get('state')
        if event.text in ['/start', '/get_list', '/set', '/reset', '/remove', '/prolong']:
            await state.clear()
        return await handler(event, data)
