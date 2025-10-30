from telebot import TeleBot
from telebot.types import ParseMode

BOT_TOKEN = "8484977548:AAFv9n_VdKc_d1Ia304UugTxRJqYqjDqMLs"  # <= токен В КАВЫЧКАХ!

if not BOT_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден!")
else:
    bot = TeleBot(BOT_TOKEN)
    print("✅ Бот запущен и слушает Telegram...")

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
        bot.send_message(message.chat.id, text, parse_mode=ParseMode.MARKDOWN)

    bot.polling(none_stop=True)


