import telebot
import os
from flask import Flask, request

# Sizning tokeningiz joylashtirildi
TOKEN = '7838831366:AAFv5D3UR4s9QdoDTLeRTD87r_d8sTAZnIs'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men Render hostingida ishlayapman. Menga rasmga aylantirish uchun PDF yoki Docx fayl yuboring!")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.reply_to(message, f"Rahmat, {message.from_user.first_name}! Faylingizni qabul qildim. Hozircha men test rejimidaman, tez orada rasmga aylantirishni ham o'rganaman.")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    # Keyingi qadamda bu yerga Render havolasini ulaymiz
    return "Bot faol!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
