import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "бот запущен и работает 👋")

# Сбрасываем вебхук, чтобы не было конфликта
bot.remove_webhook()

bot.infinity_polling()
