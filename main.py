from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8484977548:AAFv9n_VdKc_d1Ia304UugTxRJqYqjDqMLs"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
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
    await message.answer(text, parse_mode="Markdown")

if __name__ == "__main__":
    print("✅ Бот запущен...")
    executor.start_polling(dp, skip_updates=True)



