import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from routers import start_router, catalog_router, support_router

logging.basicConfig(level=logging.INFO)

async def main():

    if not BOT_TOKEN:
        raise ValueError("Не найден BOT_TOKEN. Создайте файл .env с BOT_TOKEN=ваш_токен")
    
    # инициализация
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    
    #роутеры
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(support_router)
    
    # запуск бота
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())