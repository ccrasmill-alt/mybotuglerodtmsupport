from telebot.custom_filters import StateFilter

from logger import main_logger
from config_data.config import bot
from handlers import start


if __name__ == '__main__':
    main_logger.info("Бот начал работу.")
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling(timeout=60, long_polling_timeout=60)