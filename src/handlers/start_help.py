from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from constants.bot_commands import help_command, start_command

start_help_router = Router(name=__name__)

info_message = "\n".join([
    "Привет!!", "Я - бот, который даёт ответы на игру 5 букв от Тинькофф!!",
    "Просто напиши /getword и получишь сегодняшнее слово!",
    # "Или можешь подписаться на рассылку написав /subscribe"
])


@start_help_router.message(Command(start_command, help_command))
async def start_help(message: Message):
    await message.answer(info_message)
