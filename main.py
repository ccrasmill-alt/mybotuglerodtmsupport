import telebot

# 🔒 Твой токен
TOKEN = "8484977548:AAFv9n_VdKc_d1Ia304UugTxRJqYqjDqMLs"
bot = telebot.TeleBot(TOKEN)

# 📏 Таблица размеров
sizes = [
    {"size": 42, "chest": (82, 86), "waist": (62, 66), "hips": (90, 94)},
    {"size": 44, "chest": (86, 90), "waist": (66, 70), "hips": (94, 98)},
    {"size": 46, "chest": (90, 94), "waist": (70, 76), "hips": (98, 102)},
    {"size": 48, "chest": (94, 98), "waist": (74, 78), "hips": (102, 106)},
    {"size": 50, "chest": (98, 102), "waist": (78, 82), "hips": (106, 110)},
    {"size": 52, "chest": (102, 106), "waist": (82, 86), "hips": (110, 114)},
    {"size": 54, "chest": (106, 110), "waist": (86, 90), "hips": (114, 118)},
    {"size": 56, "chest": (110, 114), "waist": (90, 94), "hips": (118, 122)},
    {"size": 58, "chest": (114, 118), "waist": (94, 98), "hips": (122, 126)},
]

# 💬 Приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 Я твой виртуальный ассистент *UGLEROD!* ✨\n\n"
        "Помогу подобрать идеальный размер без лишних хлопот.\n"
        "Мне понадобятся всего три параметра:\n\n"
        "📏 *Обхват груди*\n📏 *Обхват талии*\n📏 *Обхват бёдер*\n\n"
        "Просто введи все три значения через запятую в сантиметрах.\n\n"
        "🎯 Например: `88, 65, 92`",
        parse_mode="Markdown"
    )

# 📩 Обработка замеров
@bot.message_handler(func=lambda message: True)
def handle_size(message):
    try:
        parts = [int(x.strip()) for x in message.text.replace(',', ' ').split()]
        if len(parts) != 3:
            bot.reply_to(message, "⚠️ Введи три числа — грудь, талия, бёдра. Например: 88, 65, 92")
            return

        chest, waist, hips = parts
        result = None

        for s in sizes:
            if (s["chest"][0] <= chest <= s["chest"][1] and
                s["waist"][0] <= waist <= s["waist"][1] and
                s["hips"][0] <= hips <= s["hips"][1]):
                result = s["size"]
                break

        if result:
            bot.reply_to(message, f"🎯 Твой размер: *{result}*", parse_mode="Markdown")
        else:
            bot.reply_to(message, "😔 К сожалению, не смог определить размер по введённым параметрам. Проверь значения.")
    except Exception as e:
        bot.reply_to(message, "⚠️ Пожалуйста, введи данные корректно, например: 88, 65, 92")

# 🚀 Запуск
bot.polling(none_stop=True)

