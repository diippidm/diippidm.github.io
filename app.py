from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from credentials import BOT_TOKEN, BOT_USERNAME
import json

# Инициализация объекта application
application = ApplicationBuilder().token(BOT_TOKEN).build()

async def launch_web_ui(update: Update, callback: CallbackContext):
    kb = [
        [KeyboardButton("Show me my Web-App!", web_app=WebAppInfo("https://diippidm.github.io/"))]
    ]
    await update.message.reply_text("Let's do this...", reply_markup=ReplyKeyboardMarkup(kb))

if __name__ == "__main__":
    application.add_handler(CommandHandler('start', launch_web_ui))
    print(f"Your bot is listening! Navigate to http://t.me/{BOT_USERNAME} to interact with it!")
    application.run_polling()  # Метод для запуска приложения без необходимости вручную запускать start()
