from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

@app.on_event("startup")
async def startup_event():
    await telegram_app.initialize()
    await telegram_app.start()

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"status": "running"}
