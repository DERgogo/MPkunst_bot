import json, os

DATA_FILE = "app/data/user_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_xp(user_id, amount):
    data = load_data()
    if user_id not in data:
        data[user_id] = 0
    data[user_id] += amount
    save_data(data)

def get_xp(user_id):
    data = load_data()
    return data.get(user_id, 0)
