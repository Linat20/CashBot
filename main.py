import asyncio
import sqlite3
from aiogram import Bot, Dispatcher

from app.handlers import router

from app.database.models import async_main

async def main():
    await async_main()
    bot = Bot(token='7980650905:AAF6dn_g--EZuQoQh-ccu9qzLx4tEZlOz6k')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')