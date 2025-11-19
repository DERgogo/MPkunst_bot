from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from Handlers.menu_handler import get_handler  # oder wie auch immer der Pfad heißt

def build_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(get_handler())
    # Weitere Handler (z.B. CallbackQueryHandler für die Buttons) hier adden!
    return application
