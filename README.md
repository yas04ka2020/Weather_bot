# Weather_bot

Телеграм-бот для отримання актуальної інформації про погоду.

project "weather forecast": https://t.me/yaryna_weather_bot


## Функціонал бота

- Команда /start - Вітання користувача та опис функціоналу бота.
- Отримання поточної погоди за вказаним містом.
- Інформація про температуру, тиск, вологість, вітер та інші погодні умови.
- Відображення напрямку вітру в зрозумілому форматі.


## Інструкція з запуску "бота - погода"

### 1. Скачати проект
`git clone https://github.com/yas04ka2020/Weather_bot.git`

### 2. Перейти у папку з проектом
`cd Weather_bot`

### 3. Встановлення залежностей
`pip install -f requrements.txt`

### 4. Додати файл .env з вашим бот-токеном

Створіть .env файл у кореневій папці проєкту та додайте в нього:

BOT_TOKEN=your-telegram-bot-token
WEATHER_API_KEY=your-weather-api-key


### 5. Запустити бота

Linux/macOS:

python3 bot.py

Windows:

py bot.py


## Корисні посилання.

- Aiogram: https://docs.aiogram.dev/uk-ua/dev-3.x/dispatcher/filters/magic_filters.html
- OpenWeather API: https://openweathermap.org/
- Python dotenv: https://pypi.org/project/python-dotenv/
- Guide aiogram: https://mastergroosha.github.io/aiogram-3-guide/routers/
- Decorators: https://tproger.ru/translations/demystifying-decorators-in-python
- JSON: https://docs.python.org/uk/3/library/json.html#


## Створеня власного боту.

1. Відкрити Telegram та знайти @BotFather або у пошуку потрібно вписати наступне: https://t.me/BotFather.
2. Виконати команду /newbot. Якщо раніше вже створювали бота то можна його знайти за командою /mybots.
3. Далі вводимо username(ім’я користувача) вашого бота. 
   Обов’язково унікальне username та використовувати слово “bot” наприкінці username.    
   Наприклад: “acuta_python_awesome_first_bot”. Після чого ви отримаєте повідомлення про успішне створення вашого бота.
4. Отримати API-токен бота. Нікому не передавайте та не демонструйте цей токен!
5. Додати токен до .env файлу у вашому проєкті.


    Якщо потрібно оновити токен:
    1. Виконати /mybots у BotFather.
    2. Обрати вашого бота.
    3. Перейти у API Token.
    4. Натиснути Revoke current token та отримати новий.

Цей бот дозволяє легко отримувати актуальну погоду за будь-яким містом! 🌤️





# Weather_bot_yaryna
# Weather_bot_yaryna
