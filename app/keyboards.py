from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    cities = [
        "Lviv", "Kyiv", "Odessa", "Lutsk", "Kharkiv", "Donetsk", "Mariupol",
        "Poltava", "Luhansk", "Vinnytsia", "Zhytomyr", "Chernobyl", "Ivano-Frankivsk",
        "Cherkasy", "Kryvyi Rih", "Chernivtsi", "Ternopil", "Dnepropetrovsk",
        "Chernihiv", "Lizhorod"
    ]
    
    for city in cities:
        builder.button(text=city)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup

