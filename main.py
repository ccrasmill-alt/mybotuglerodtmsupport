import os
from telebot import TeleBot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден! Добавь переменную окружения BOT_TOKEN на Bothost.")
else:
    bot = TeleBot(BOT_TOKEN, parse_mode="Markdown")

    @bot.message_handler(commands=["start"])
    def start(message):
        text = (
            "Я твой виртуальный ассистент *UGLEROD!* ✨\n\n"
            "Помогу подобрать идеальный размер без лишних хлопот. Для этого мне понадобятся всего три параметра:\n\n"
            "📏 *Обхват груди*\n"
            "📏 *Обхват талии*\n"
            "📏 *Обхват бёдер*\n\n"
            "Просто введи все три значения через запятую в сантиметрах.\n\n"
            "🎯 *Например:* 88, 65, 92\n\n"
            "Готов(а) начать? Жду твои замеры! 👇"
        )
        bot.send_message(message.chat.id, text)

    print("✅ Бот запущен и ждёт сообщений...")
    bot.polling(none_stop=True)

