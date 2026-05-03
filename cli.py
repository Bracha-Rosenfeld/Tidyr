import argparse
from organizer import mover
from organizer.watcher import watch

parser = argparse.ArgumentParser(prog="tidyr")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--run", metavar="FOLDER", help="organize a folder")
group.add_argument("--watch", metavar="FOLDER", help="watch a folder continuously")
group.add_argument("--undo", action="store_true", help="undo last run")
parser.add_argument("--dry-run", action="store_true", help="preview without moving")

args = parser.parse_args()

if args.undo:
    mover.undo()
elif args.watch:
    watch(args.watch)
else:
    mover.run(args.run, dry_run=args.dry_run)
