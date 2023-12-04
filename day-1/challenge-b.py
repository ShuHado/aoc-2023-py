file = open("day-1/input.txt", "r")
input = file.read().split("\n")

file.close()

digitWords = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calibrationValue(line):
    first = None
    last = None
    buffer = ""
    for char in line:
        value = char
        if value.isalpha():
            buffer += char
            hasFoundWordDigit = False
            for word in digitWords.keys():
                if buffer.startswith(word) or buffer.endswith(word):
                    value = digitWords[word]
                    buffer = buffer[-1:]
                    hasFoundWordDigit = True
            if not hasFoundWordDigit:
                continue
        if first is None:
            first = value
        last = value
    return int(str(first) + str(last))


def run():
    total = 0
    for line in input:
        total += calibrationValue(line)
    return total
