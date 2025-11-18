from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_TOKEN

# Build bot instance
app = ApplicationBuilder().token(BOT_TOKEN).build()

# --- Start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 MPkunst Bot aktiviert!\n"
        "Willkommen im 0711 Trap Menü.\nTippe: /menu"
    )

# Register handlers
app.add_handler(CommandHandler("start", start))
