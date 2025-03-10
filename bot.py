import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types.bot_command import BotCommand
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN_BOT")

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands([
        BotCommand(command="start", description="Зaпуск ботa"),
    ])

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filemode="w",
        filename="botlog.log",
    )
    asyncio.run(main())
    