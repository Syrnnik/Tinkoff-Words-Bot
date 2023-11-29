import schedule
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from constants.bot_commands import stop_command
from loader import dp


@dp.message(stop_command)
async def stop(message: Message, state: FSMContext):
    user_state = await state.get_state()
    if not user_state:
        await message.answer("Вы не были подписаны на рассылку ответов")
    else:
        await message.answer("Вы отписались от рассылки ответов")
        await state.clear()

        chat_id = message.chat.id
        user_jobs = schedule.get_jobs(chat_id)
        if len(user_jobs) != 0:
            schedule.cancel_job(user_jobs[0])
