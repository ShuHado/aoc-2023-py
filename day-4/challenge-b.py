file = open("day-4/input.txt", "r")
input = file.readlines()
file.close()


def cardPoints(line, index):
    nb_win_numbers = 0
    line = line.removeprefix(f"Card {index}: ").split("\n")
    line = line[0].split("|")
    win_numbers = [x for x in line[0].split(" ") if x != ""]
    my_numbers = [x for x in line[1].split(" ") if x != ""]
    for number in my_numbers:
        if number in win_numbers:
            nb_win_numbers += 1
    return nb_win_numbers


def run():
    cards = {x: 1 for x in range(1, len(input) + 1)}
    total = 0
    for line in input:
        index = input.index(line) + 1
        nb_wins = cardPoints(line, index)
        if nb_wins > 0:
            for i in range(index, index + nb_wins + 1):
                if i == index:
                    cards[i] = cards[i]
                elif index == 1:
                    cards[i] += cards[index]
                else:
                    cards[i] += cards[index]
    for card in cards:
        total += cards[card]
    return total


print("Total : ", run())
