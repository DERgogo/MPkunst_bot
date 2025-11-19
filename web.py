from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

app = FastAPI()  # <--- HEISST 'app', nicht 'api'

tg_app = ApplicationBuilder().token(BOT_TOKEN).build()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return {"status": "ok"}


@app.get("/")
def home():
    return {"status": "running"}
