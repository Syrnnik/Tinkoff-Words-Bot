from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.constants.bot_commands import getword_command
from src.utils.api.words_api import get_today_word

get_word_router = Router(name=__name__)


@get_word_router.message(Command(getword_command))
async def get_word(message: Message):
    today_word = get_today_word()
    await message.answer(f"Сегодняшнее слово: {today_word}")
