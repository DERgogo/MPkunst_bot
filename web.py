from fastapi import FastAPI, Request
from bot import app
from telegram import Update

api = FastAPI()

@api.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, app.bot)
    await app.process_update(update)
    return {"status": "ok"}
