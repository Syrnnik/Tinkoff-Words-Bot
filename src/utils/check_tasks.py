import asyncio

import schedule


async def run_tasks_checking():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
