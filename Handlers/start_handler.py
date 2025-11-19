
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Car-BonMP", callback_data="car_bon")],
        [InlineKeyboardButton("🎨 GogoMP", callback_data="gogo_mp")],
        [InlineKeyboardButton("📈 XP-Status anzeigen", callback_data="xp_status")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_msg = """
🏙️ *Willkommen beim S0711CITYBOT®*  
_Dein digitaler Zugang zu Visual Art & Dental Game in 0711-TRAP-Vibes_

🔥 *Wähle eine Zone:*
    """
    await update.message.reply_markdown(welcome_msg, reply_markup=reply_markup)

def get_handler():
    return CommandHandler("start", start)
