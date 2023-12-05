file = open("day-4/input.txt", "r")
input = file.readlines()
file.close()


def cardPoints(line, index):
    nb_win_numbers = 0
    line = line.removeprefix(f"Card {index+1}: ").split("\n")
    line = line[0].split("|")
    win_numbers = [x for x in line[0].split(" ") if x != ""]
    my_numbers = [x for x in line[1].split(" ") if x != ""]
    for number in my_numbers:
        if number in win_numbers:
            nb_win_numbers += 1
    return int(1 * 2**(nb_win_numbers-1))


def run():
    total = 0
    for line in input:
        index = input.index(line)
        total += cardPoints(line, index)
    return total