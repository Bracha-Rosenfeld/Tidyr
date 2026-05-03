import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer.config import load_rules
from organizer.mover import resolve_dest_folder
from organizer.logger import log_move, commit_session

class TidyrHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()
        rules = load_rules()
        if ext not in rules:
            print(f"⏭️  {filename}  →  no rule, skipped")
            return
        dest_folder = resolve_dest_folder(rules[ext])
        dest = os.path.join(dest_folder, filename)
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(filepath, dest)
        log_move(filepath, dest)
        commit_session()
        print(f"✅ {filename}  →  {dest_folder}")

def watch(folder):
    observer = Observer()
    observer.schedule(TidyrHandler(), folder, recursive=False)
    observer.start()
    print(f"👀 watching {folder} — press Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()