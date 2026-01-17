import telebot
import os
from flask import Flask, request

TOKEN = '7838831366:AAFv5D3UR4s9QdoDTLeRTD87r_d8sTAZnIs'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    # HTML formatida xabar yuborish
    text = (
        "<b>Salom, xush kelibsiz!</b>\n\n"
        "Men <i>Render</i> hostingida muvaffaqiyatli ishlayapman.\n"
        "Sizga yordam berishdan xursandman! 😊\n\n"
        "<a href='https://t.me/BotFather'>BotFather</a> orqali botingizni sozlaganingiz uchun rahmat."
    )
    bot.reply_to(message, text, parse_mode='HTML')

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    return "Bot serveri faol va HTML-ni tushunadi!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
