import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router
from DataBase import create_db

token = open("token.txt", "r").readline().strip()

async def main() -> None:
    bot = Bot(token=token, parse_mode="Markdown")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    create_db()
    print("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
