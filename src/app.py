import asyncio

from aiogram import Bot

from loader import dp, bot
from utils.bot.set_bot_commands import set_bot_commands
from utils.bot.set_bot_routers import set_bot_routers


async def on_startup(bot: Bot):
    set_bot_routers(dp)
    await set_bot_commands(bot)
    print("I'm ready!")


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
