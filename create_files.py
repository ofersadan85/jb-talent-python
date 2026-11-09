from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("number", type=int, help="Number of files")
parser.add_argument("folder", type=Path, default=Path(), nargs="?")
# parser.add_argument("-x", "--extension", default=["txt"], nargs="*")  # 0 or more
parser.add_argument("-x", "--extension", default=["txt"], nargs="+")  # 1 or more
parser.add_argument("-p", "--print", action="store_true")

# group = parser.add_argument_group("Image size")
# group.add_argument("--width")
# group.add_argument("--height")
# group2 = parser.add_mutually_exclusive_group()
# group2.add_argument("--width")
# group2.add_argument("--height")
args = parser.parse_args()

print(args)

files = ["1.txt", "z.exe", "b.pdf", "y.exe", "2.txt"]

args.folder.mkdir(exist_ok=True)
for i in range(1, args.number + 1):
    for ext in args.extension:
        p = args.folder / Path(str(i) + "." + ext)
        p.touch()
        if args.print:
            print("Created", p)
