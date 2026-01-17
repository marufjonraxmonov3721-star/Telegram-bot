from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("7838831366:AAFv5D3UR4s9QdoDTLeRTD87r_d8sTAZnIs")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom aka 👋 Bot Render’da ishlayapti ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
python-telegram-bot==20.7
services:
  - type: worker
    name: telegram-bot
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
