from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("--reverse", action="store_true")
parser.add_argument("folder", type=Path, default=Path(), nargs="?")
args = parser.parse_args()

print(args)

# files = ["1.txt", "z.exe", "b.pdf", "y.exe", "2.txt"]
# files = []
# for f in args.folder.iterdir():
#     files.append(f)
files = list(args.folder.iterdir())

if args.sort:
    files.sort()

if args.reverse:
    files.reverse()

if args.l:
    for f in files:
        print(f.name)
else:
    # print(files)
    for f in files:
        print(f.name, end=" ")
    print()
