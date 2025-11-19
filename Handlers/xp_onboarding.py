from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from app.services.xp_manager import add_xp, get_xp

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = str(query.from_user.id)
    await query.answer()

    if query.data == "car_bon":
        add_xp(user_id, 10)
        await query.edit_message_text("💎 Willkommen bei Car-BonMP – +10 XP")

    elif query.data == "gogo_mp":
        add_xp(user_id, 10)
        await query.edit_message_text("🎨 Willkommen bei GogoMP – +10 XP")

    elif query.data == "xp_status":
        xp = get_xp(user_id)
        await query.edit_message_text(f"📈 Dein aktueller XP-Stand: *{xp} XP*", parse_mode="Markdown")

def get_handler():
    return CallbackQueryHandler(handle_callback)
