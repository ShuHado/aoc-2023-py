import argparse

parser = argparse.ArgumentParser(
    prog="python app.py",
    description="Run the program corresponding to the day who is passed as argument",
)

parser.add_argument("-d", "--day", type=int, help="Day of the challenge", required=True)
parser.add_argument(
    "-p",
    "--part",
    type=str,
    help="Part of the challenge",
    required=True,
    choices=["a", "b"],
)

args = parser.parse_args()

if args.part == "a":
    exec(open(f"day-{args.day}/challenge-a.py").read())
elif args.part == "b":
    exec(open(f"day-{args.day}/challenge-b.py").read())
