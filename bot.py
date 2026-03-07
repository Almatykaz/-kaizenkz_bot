import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="Алға ➡️",
        web_app=WebAppInfo(url="https://luxury-kelpie-238096.netlify.app/")
    ))
    await message.answer(
        "📚 Қаржы сауаттылық сабағына қош келдіңіз!\n\nСабақты бастау үшін — Алға кнопкасын басыңыз 👇",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
```

Сосын **requirements.txt** файлын:
```
aiogram==2.25.1
