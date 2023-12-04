file = open("day-2/input.txt", "r")
input = file.readlines()
file.close()

colors = ["red", "green", "blue"]


def run():
    total = 0
    for line in input:
        colorMax = {"red": 0, "green": 0, "blue": 0}
        line = line.strip()
        line = line.split(":")
        line[1] = line[1].split(";")
        line = line[1]
        for set in line:
            set = set.split(",")
            for entry in set:
                entry = entry.strip()
                entry = entry.split(" ")
                value = int(entry[0])
                entry_color = entry[1]
                for color in colors:
                    if color == entry_color:
                        colorMax[color] = max(colorMax[color], value)
        total += colorMax["red"] * colorMax["green"] * colorMax["blue"]
    return total