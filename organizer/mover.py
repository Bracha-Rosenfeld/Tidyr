import os
import shutil
import winreg
from organizer.config import load_rules
from organizer.logger import log_move, load_log, clear_log

SHELL_FOLDERS_KEY = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"

WINDOWS_FOLDER_KEYS = {
    "PICTURES": "My Pictures",
    "DOCUMENTS": "Personal",
    "MUSIC": "My Music",
    "VIDEOS": "My Video",
    "DESKTOP": "Desktop",
}

def get_windows_folder(name):
    key = name.upper()
    if key not in WINDOWS_FOLDER_KEYS:
        return None
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, SHELL_FOLDERS_KEY) as reg:
        path, _ = winreg.QueryValueEx(reg, WINDOWS_FOLDER_KEYS[key])
    return path

def resolve_dest_folder(rule_folder):
    # if it's a known Windows folder key, resolve it
    windows_path = get_windows_folder(rule_folder)
    if windows_path:
        return windows_path
    # otherwise put it on the Desktop
    desktop = get_windows_folder("DESKTOP")
    return os.path.join(desktop, rule_folder)

def run(folder, dry_run=False):
    rules = load_rules()
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if not os.path.isfile(filepath):
            continue
        ext = os.path.splitext(filename)[1].lower()
        if ext not in rules:
            print(f"⏭️  {filename}  →  no rule, skipped")
            continue
        dest_folder = resolve_dest_folder(rules[ext])
        dest = os.path.join(dest_folder, filename)
        if dry_run:
            print(f"🔍 {filename}  →  {dest_folder}")
        else:
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(filepath, dest)
            log_move(filepath, dest)
            print(f"✅ {filename}  →  {dest_folder}")

def undo():
    moves = load_log()
    if not moves:
        print("nothing to undo.")
        return
    for entry in reversed(moves):
        if os.path.exists(entry["dst"]):
            shutil.move(entry["dst"], entry["src"])
            print(f"↩️  {os.path.basename(entry['dst'])}  →  restored")
    clear_log()
