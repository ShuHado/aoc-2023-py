import argparse
import importlib

parser = argparse.ArgumentParser(
    prog="python app.py",
    description="Run the program corresponding to the day who is passed as argument",
)

parser.add_argument(
    "-d",
    "--day",
    type=int,
    help="Day of the challenge",
    required=True,
    choices=range(1, 26),
)

args = parser.parse_args()

resultA = importlib.import_module(f"day-{args.day}.challenge-a").run()
resultB = importlib.import_module(f"day-{args.day}.challenge-b").run()

print(f"Day {args.day} \u2744\uFE0F")
print(f"Challenge A \U0001F385 : {resultA}")
print(f"Challenge A \U0001F385 : {resultB}")
