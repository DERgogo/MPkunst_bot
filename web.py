from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

app = FastAPI()

# TELEGRAM BOT INITIALISIERUNG
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)

    # BOT INITIALISIERUNG FIX
    if not telegram_app.running:
        await telegram_app.initialize()
        await telegram_app.start()
    
    await telegram_app.process_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "running", "webhook": "/webhook"}
