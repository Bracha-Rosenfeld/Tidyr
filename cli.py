import os

folder = "/Users/yourname/Downloads"  # change this to a real folder

for filename in os.listdir(folder):
    name, ext = os.path.splitext(filename)
    print(f"{filename}  →  extension: {ext}")