import asyncio
import logging
import math
import os
import sys
from math import degrees

import requests
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, URLInputFile
from aiogram.types.bot_command import BotCommand
from dotenv import load_dotenv
from keyboards import menu_keyboard
from keys import weather_key

from logging_tool import async_log_handlers, logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

load_dotenv(".env")

TOKEN = os.getenv("TOKEN_BOT")
WEATHER_KEY = os.getenv("weather_key")


router = Router()
DATABASE = "data.json"

logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

# command  /start


@dp.message(CommandStart())
@async_log_handlers
async def start_command(message: Message, *args, **kwargs) -> None:

    await message.answer(
        f"Hello, {message.from_user.id}:{message.from_user.full_name}! "
    )
    await message.answer(
        "Type the city name or Use one from the list", reply_markup=menu_keyboard()
    )
    logger.info("START is Ok")


# list of weather


@dp.message(F.text)
@async_log_handlers
async def get_weather(message: types.Message):
    city = message.text
    try:
        complete_url = f"{BASE_URL}q={city}&appid={weather_key}&units=metric"
        weather_response = requests.get(complete_url)

        data = weather_response.json()
        if weather_data["cod"] == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]
            wind_data = data["wind"]

            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]
            wind_speed = wind_data["speed"]

            weather_report = (
                f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Pressure: {pressure} hPa\n"
                f"Humidity: {humidity}%\n"
                f"Weather: {weather_description.capitalize()}\n"
                f"Wind Speed: {wind_speed} m/s"
            )

            def wind_direction(degrees):
                directions = [
                    "North",
                    "North-East",
                    "East",
                    "South-East",
                    "South",
                    "South-West",
                    "West",
                    "North-West",
                ]

            index = int((degrees + 22.5) // 45) % 8
            return index

            await message.reply(weather_report)
        else:
            await message.reply("City not found!")
    except Exception as e:
        print(e)
        await message.reply("Something went wrong")


async def main() -> None:

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Run the bot"),
        ]
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
