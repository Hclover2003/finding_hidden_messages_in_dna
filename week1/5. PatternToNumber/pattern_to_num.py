import sys
with open(sys.argv[1], "r") as file:
    data = file.read()
    data = data.strip()
    print(data)


def letter_to_num(letter):
    letter = letter.lower()
    if letter == 'a':
        return 0
    elif letter == 'c':
        return 1
    elif letter == 'g':
        return 2
    elif letter == 't':
        return 3
    else:
        raise Exception("Not a valid letter")


def pattern_to_num(input):
    if len(input) == 1:
        return 0
    lastletter = input[-1]
    prefix = input[:-1]
    return 4*pattern_to_num(prefix) + letter_to_num(lastletter)


result = pattern_to_num(data)
print(result)
