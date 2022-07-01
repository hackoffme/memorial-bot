import asyncio
from tbot.config import load_config
from aiogram import Bot, Dispatcher

from tbot.handlers.user import register_user


def register_all_handlers(dp):
    register_user(dp)


async def main():
    config = load_config()
    bot = Bot(token=config.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as err:
        print(err)
