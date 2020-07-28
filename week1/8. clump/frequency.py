import sys

with open(sys.argv[1], "r") as file:
    dna = file.readlines()
    text = dna[0].strip()
    k = int(dna[1].strip())


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
    if len(input) == 0:
        return 0
    lastletter = input[-1]
    prefix = input[:-1]
    return 4*pattern_to_num(prefix) + letter_to_num(lastletter)


def compute_frequency(text, k):
    freq_array = []
    # index 0 - 4^k - 1 (for all the possiblilities, fill array with 0)
    for i in range(0, 4**k):
        freq_array.append(0)
    # if len text was 5, index 0-4, k was 2. want it to include index 3, stop at 4
    #thus, 5-(2-1)
    for i in range(0, len(text) - k+1):
        # if 0, slice from 0 - 0+1
        pattern = text[i:i+k]
        index = pattern_to_num(pattern)
        freq_array[index] += 1
    return freq_array


result = compute_frequency(text, k)

with open(sys.argv[2], "w") as results:
    for i in range(0, len(result)):
        results.write(str(result[i]) + " ")
