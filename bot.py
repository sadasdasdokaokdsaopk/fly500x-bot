from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("FLY500X.jpg", "rb") as photo:
        keyboard = [[InlineKeyboardButton("Зарегистрироваться", url="https://1wzyuh.com/casino/list?open=register&p=xu4f")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(photo=photo, caption="🎁 Промокод: FLY500X", reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, start))
    app.run_polling()

if __name__ == "__main__":
    main()
