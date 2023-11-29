from aiogram import Dispatcher

from src.handlers.get_word import get_word_router
from src.handlers.start_help import start_help_router


def set_bot_routers(dispatcher: Dispatcher):
    dispatcher.include_router(start_help_router)
    dispatcher.include_router(get_word_router)
