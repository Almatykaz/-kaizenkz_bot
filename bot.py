import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "МҰНДА_ӨЗ_ТОКЕНІҢІЗ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="Алға ➡️",
            web_app=WebAppInfo(url="https://luxury-kelpie-238096.netlify.app/")
        )
    ]])
    await message.answer(
        "📚 Қаржы сауаттылық сабағына қош келдіңіз!\n\nСабақты бастау үшін — Алға кнопкасын басыңыз 👇",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())