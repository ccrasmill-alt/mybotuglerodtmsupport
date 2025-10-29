import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()  # <-- добавляем эту строку, чтобы BotHost подхватил BOT_TOKEN

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("Ошибка: BOT_TOKEN не найден! Добавь переменную окружения BOT_TOKEN на Bothost.")
else:
    bot = TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Я бот 👕 Помогаю определить размер одежды!")

    print("✅ Бот запущен и слушает Telegram...")
    bot.polling(none_stop=True)
