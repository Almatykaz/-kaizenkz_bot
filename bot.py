import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="Алға ➡️",
        web_app=WebAppInfourl="https://graceful-peony-98922f.netlify.app/")
    ))
    bot.send_message(
        message.chat.id,
        "📚 Қаржы сауаттылық сабағына қош келдіңіз!\n\nСабақты бастау үшін — Алға кнопкасын басыңыз 👇",
        reply_markup=keyboard
    )

bot.infinity_polling()

