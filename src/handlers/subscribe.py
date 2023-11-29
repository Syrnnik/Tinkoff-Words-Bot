import schedule
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.constants.bot_commands import subscribe_command
from loader import dp
from src.states.UserStates import UserState
from src.utils.send_word_to_subscribed_user import send_word_to_subscribed_user


@dp.message(subscribe_command)
async def subscribe(message: Message, state: FSMContext):
    user_state = await state.get_state()
    if user_state == "UserState:subscribed":
        await message.answer("Вы уже подписаны на рассылку ответов")
    else:
        await message.answer("Вы подписались на рассылку ответов")
        await UserState.subscribed.set()

        chat_id = str(message.chat.id)
        schedule.every(10).seconds.do(
            send_word_to_subscribed_user,
            chat_id=chat_id
        ).tag(chat_id)
