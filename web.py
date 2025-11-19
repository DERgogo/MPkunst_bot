from fastapi import FastAPI, Request
from telegram import Update
from bot import app

api = FastAPI()

@api.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, app.bot)
    await app.process_update(update)
    return {"status": "ok"}
