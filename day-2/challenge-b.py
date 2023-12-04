file = open("day-2/input.txt", "r")
input = file.readlines()
file.close()

total = 0

colors = ["red", "green", "blue"]

for line in input:
    redMax = 0
    greenMax = 0
    blueMax = 0
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
                    globals()[color + "Max"] = max(globals()[color + "Max"], value)
    total += redMax * greenMax * blueMax

print(f"Challenge B \U0001F385 : {total}")
