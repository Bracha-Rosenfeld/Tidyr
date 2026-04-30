import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

def load_rules():
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)
    # flatten: { ".pdf": "Documents", ".jpg": "Images", ... }
    rules = {}
    for folder, extensions in data["rules"].items():
        for ext in extensions:
            rules[ext.lower()] = folder
    return rules
