# 📁 Tidyr

*because your downloads folder is a crime scene and someone had to say it.*

---

your files are a mess. `.pdf` living next to a meme from 2019, three files named `final_FINAL_v2.png`. 
Tidyr fixes that. automatically. while you do literally anything else.

---

## what it does

- 👀 watches your folder like a hawk (a very organized hawk)
- 📂 moves files into the right subfolder the second they land
- ↩️ undo in one command, no questions asked
- 🔍 dry run mode — look before you leap
- 📋 keeps a log, so you can see exactly what it touched

---

## get started

```bash
git clone https://github.com/your-username/tidyr
cd tidyr
pip install -r requirements.txt
```

that's it. you're basically a developer now.

---

## how to use it

```bash
# set it and forget it
python cli.py --watch C:\Users\YourName\Downloads

# organize what's already there
python cli.py --run C:\Users\YourName\Downloads

# see what *would* happen (for the anxious girlies)
python cli.py --run C:\Users\YourName\Downloads --dry-run

# oops
python cli.py --undo
```

---

## make it yours

open `config.yaml` and define your own rules:

```yaml
rules:
  DOCUMENTS: [.pdf, .docx, .txt]
  PICTURES:  [.jpg, .jpeg, .png, .gif, .webp]
  VIDEOS:    [.mp4, .mov, .mkv]
  MUSIC:     [.mp3, .flac]
  Desktop/Code:     [.py, .js, .html]
  Desktop/Archives: [.zip, .rar]
```

> uppercase keys like `DOCUMENTS` and `PICTURES` resolve to your actual Windows folders. anything else gets created on your Desktop.

no rules you didn't write.

---

## built with

python · watchdog · pyyaml · a deep hatred of cluttered folders

---

*MIT license — free to use, free to judge your own file organization*
