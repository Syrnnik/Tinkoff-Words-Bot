from aiogram import Bot

from constants.bot_commands import help_command, getword_command


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands([
        help_command,
        getword_command,
        # subscribe_command,
        # stop_command
    ])
