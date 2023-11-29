from aiogram.types import BotCommand

help_command = BotCommand(
    command="help",
    description="Узнать информацию о боте",
)

start_command = BotCommand(
    command="start",
    description="Начать общение с ботом",
)

getword_command = BotCommand(
    command="getword",
    description="Получить сегодняшнее слово"
)

subscribe_command = BotCommand(
    command="subscribe",
    description="Подписаться на рассылку ответов на Тинькофф 5 слов"
)

stop_command = BotCommand(
    command="stop",
    description="Отписаться от рассылки ответов на Тинькофф 5 слов"
)
