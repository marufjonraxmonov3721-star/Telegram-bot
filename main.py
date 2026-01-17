import telebot
import os
from flask import Flask, request

# Sizning tokeningiz
TOKEN = '7838831366:AAFv5D3UR4s9QdoDTLeRTD87r_d8sTAZnIs'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men nihoyat ishladim! 😊\nEndi menga fayl yuborsangiz bo'ladi.")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    return "Bot serveri ishlamoqda!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
