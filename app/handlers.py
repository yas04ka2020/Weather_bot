import asyncio
import logging
import os
import sys

import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.bot_command import BotCommand
from dotenv import load_dotenv
from keyboards import menu_keyboard
from logging_tool import async_log_handlers, logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

load_dotenv(".env")

TOKEN = os.getenv("TOKEN_BOT")
WEATHER_KEY = os.getenv("weather_key")

bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


# command  /start
@dp.message(CommandStart())
@async_log_handlers
async def start_command(message: Message, *args, **kwargs) -> None:
    await message.answer(f"Hello, {message.from_user.id}:{message.from_user.full_name}! ")
    await message.answer(
        "Type the city name or Use one from the list", reply_markup=menu_keyboard()
    )
    logger.info("START is Ok")


# list of weather
def wind_direction(degrees: float) -> str:
    directions = [
        "North", "North-East", "East", "South-East",
        "South", "South-West", "West", "North-West",
    ]
    index = int((degrees + 22.5) // 45) % 8
    return directions[index]


@dp.message(F.text)
@async_log_handlers
async def get_weather(message: types.Message, *args, **kwargs) -> None:
    city = message.text
    complete_url = f"{BASE_URL}q={city}&appid={WEATHER_KEY}&units=metric"
    weather_response = requests.get(complete_url)
    data = weather_response.json()
    
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data["wind"]

        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]
        wind_speed = wind_data["speed"]         
        direction_wind = wind_direction(wind_data["deg"])
        
        weather_report = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather_description.capitalize()}\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Direction wind: {direction_wind}"
        )
        await message.reply(weather_report)
    else:
        await message.reply("City not found!")


async def main() -> None:
    await bot.set_my_commands([
        BotCommand(command="start", description="Run the bot"),
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
