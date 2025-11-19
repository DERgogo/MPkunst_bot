from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from Handlers.menu_handler import start, get_handlers

def build_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    for handler in get_handlers():
        application.add_handler(handler)
    return application
