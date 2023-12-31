file = open("day-2/input.txt", "r")
input = file.readlines()
file.close()

redMax = 12
greenMax = 13
blueMax = 14

colors = ["red", "green", "blue"]


def run():
    total = 0
    for line in input:
        line = line.strip()
        line = line.split(":")
        line[0] = line[0].split(" ")
        line[1] = line[1].split(";")
        isPossible = True
        for set in line[1]:
            set = set.split(",")
            for entry in set:
                entry = entry.strip()
                entry = entry.split(" ")
                for color in colors:
                    if color in entry:
                        if int(entry[0]) > eval(f"{color}Max"):
                            isPossible = False
        if isPossible:
            total += int(line[0][1])
    return total
