import logging

from app.handlers import common
from config.config import Settings
from app.bot import create_bot
from app.database.base import Database


async def main():
    logging.basicConfig(level=logging.INFO)

    config = Settings()
    bot, dp = create_bot(config)
    database = Database(config.DB_URL)

    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
