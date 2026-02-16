import asyncio
import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)

    async with Bot(token=BOT_TOKEN) as bot:
        await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())