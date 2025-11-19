import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
APP_URL = os.getenv("APP_URL", "")
WEBHOOK_URL = f"{APP_URL}/webhook"
