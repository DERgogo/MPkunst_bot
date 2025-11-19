import json
from pathlib import Path

DATA_FILE = Path("data/xp.json")

def load_xp():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_xp(data):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_xp(user_id, amount):
    data = load_xp()
    data[user_id] = data.get(user_id, 0) + amount
    save_xp(data)

def get_xp(user_id):
    return load_xp().get(user_id, 0)
