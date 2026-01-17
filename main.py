import telebot
import os
from flask import Flask, request

# Tokeningiz
TOKEN = '7838831366:AAFv5D3UR4s9QdoDTLeRTD87r_d8sTAZnIs'
# Render havolangiz (oxirida / belgisiz)
APP_URL = 'https://telegram-bot-97v7.onrender.com'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Mana endi men aniq ishlayapman! 😊\nMenga PDF yoki Word fayl yuboring.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.reply_to(message, "Faylni oldim! Tez orada uni rasmga aylantirishni o'rganib olaman.")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL + '/' + TOKEN)
    return "Bot ishlashga tayyor!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
