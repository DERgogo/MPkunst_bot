from fastapi import FastAPI, Request
from telegram import Update
from bot import build_bot

app = FastAPI()
telegram_app = build_bot()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "running"}
