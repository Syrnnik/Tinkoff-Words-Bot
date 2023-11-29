import asyncio

from loader import bot
from src.utils.api.words_api import get_today_word


def send_word_to_subscribed_user(chat_id: int):
    today_word = get_today_word()
    coro = bot.send_message(chat_id, f"Сегодняшнее слово: {today_word}")
    # loop = asyncio.new_event_loop()
    # loop.run_until_complete()
    asyncio.create_task(
        bot.send_message,
        chat_id,
        f"Сегодняшнее слово: {today_word}"
    )
