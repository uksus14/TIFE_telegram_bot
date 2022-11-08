# Использование .env файлов в проекте с какими-либо паролями - хорошая практика
# Таким образом никакие пароли не попадут в интернет
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")

# простой эхо бот
import telebot
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "start")

@bot.message_handler(content_types=["text"])
def start(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()