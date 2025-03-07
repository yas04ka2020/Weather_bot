from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
    ReplyKeyboardBuilder,
)

PAGE_SIZE = 5

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="Lviv")
    builder.button(text="Kyiv")
    builder.button(text="Odessa")
    builder.button(text="Lutsk")
    builder.button(text="Kharkiv")
    builder.button(text="Donetsk")
    builder.button(text="Mariupol")
    builder.button(text="Poltava")
    builder.button(text="Luhansk")
    builder.button(text="Vinnytsia")
    builder.button(text="Zhytomyr")
    builder.button(text="Chernobyl")
    builder.button(text="Ivano-Frankivsk")
    builder.button(text="Cherkasy")
    builder.button(text="Kryvyi Rih")
    builder.button(text="Chernivtsi")
    builder.button(text="Ternopil")
    builder.button(text="Dnepropetrovsk")
    builder.button(text="Chernihiv")
    builder.button(text="Lizhorod")

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


class WeatherCallback(CallbackData, prefix="weather", sep=";"):
    id: int
    title: str


def film_keyboard(weather_list: list[dict], page: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    total_pages = (len(weather_list) + PAGE_SIZE - 1) // PAGE_SIZE
    start_idx = (page - 1) * PAGE_SIZE
    end_idx = start_idx + PAGE_SIZE

    for index, weather_data in enumerate(
        weather_list[start_idx:end_idx], start=start_idx
    ):
        callback_weather = WeatherCallback(id=index, **weather_data)
        builder.button(
            text=f"{callback_weather.name}", callback_data=callback_weather.pack()
        )
        builder.adjust(1, repeat=True)

    nav_buttons = []

    if page > 1:
        nav_buttons.append(
            InlineKeyboardButton(text="< Назад", callback_data=f"page_{page - 1}")
        )
    if page < total_pages:
        nav_buttons.append(
            InlineKeyboardButton(text="Вперед >", callback_data=f"page_{page + 1}")
        )

    if nav_buttons:
        builder.row(*nav_buttons)

    return builder.as_markup()
