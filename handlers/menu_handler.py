from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from services.xp_manager import add_xp, get_xp

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("💎 Car-BonMP", callback_data="car_bon")],
    [InlineKeyboardButton("🎨 GogoMP", callback_data="gogo_mp")],
    [InlineKeyboardButton("📈 XP-Stand anzeigen", callback_data="xp_status")]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🚀 *Welcome zum MPkunst Bot*\n"
        f"Trap trifft Kreativität.\n\n"
        f"Wähle deinen Bereich & sammle XP!\n\n"
        f"_0711 Allstars – Car-BonMP & GogoMP_",
        reply_markup=MAIN_MENU,
        parse_mode="Markdown"
    )

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = str(query.from_user.id)
    await query.answer()

    if query.data == "car_bon":
        add_xp(user_id, 10)
        await query.edit_message_text("💎 Willkommen bei *Car-BonMP*!\n(+10 XP)", parse_mode="Markdown", reply_markup=MAIN_MENU)

    elif query.data == "gogo_mp":
        add_xp(user_id, 10)
        await query.edit_message_text("🎨 Willkommen bei *GogoMP*!\n(+10 XP)", parse_mode="Markdown", reply_markup=MAIN_MENU)

    elif query.data == "xp_status":
        xp = get_xp(user_id)
        await query.edit_message_text(
            f"📈 *Dein aktueller XP-Stand:*\n\n`{xp} XP`\n\nTrap weiter & sammle mehr XP!",
            parse_mode="Markdown",
            reply_markup=MAIN_MENU
        )

def get_handlers():
    return [
        CallbackQueryHandler(handle_menu)
    ]
