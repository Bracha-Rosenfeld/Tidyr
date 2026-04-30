import json
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "organizer.log")

def log_move(src, dst):
    entry = {"src": src, "dst": dst}
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

def load_log():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def clear_log():
    open(LOG_PATH, "w").close()
