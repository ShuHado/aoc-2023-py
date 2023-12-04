file = open("day-1/input.txt", "r")
input = file.readlines()

file.close()

output = []
word = ""

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j].isdigit():
            word += input[i][j]
        elif input[i][j] == "\n":
            output.append(word)
            word = ""

for i in range(len(output)):
    if len(output[i]) == 1:
        output[i] += output[i]
    elif len(output[i]) == 2:
        pass
    elif len(output[i]) > 2:
        output[i] = output[i][0] + output[i][-1]

def run():
    total = 0
    for i in range(len(output)):
        total += int(output[i])
    return total