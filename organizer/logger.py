import json
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "organizer.log")

_current_session = []

def log_move(src, dst):
    _current_session.append({"src": src, "dst": dst})

def commit_session():
    if not _current_session:
        return
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(_current_session) + "\n")
    _current_session.clear()

def load_log():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        lines = [line for line in f if line.strip()]
    return json.loads(lines[-1]) if lines else []

def pop_log():
    if not os.path.exists(LOG_PATH):
        return
    with open(LOG_PATH, "r") as f:
        lines = [line for line in f if line.strip()]
    with open(LOG_PATH, "w") as f:
        f.writelines(lines[:-1])
