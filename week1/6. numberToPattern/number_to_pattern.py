import sys
import math

with open(sys.argv[1], "r") as file:
    data = file.readlines()
    dna = int(data[0])
    k = int(data[1])


def Remainder(num, quotient):
    return num - (quotient*4)


def Quotient(num):
    return math.floor(num/4)


def digit_to_letter(digit):
    if digit == 0:
        return 'a'
    elif digit == 1:
        return 'c'
    elif digit == 2:
        return 'g'
    elif digit == 3:
        return 't'
    else:
        raise Exception("Not a valid digit")


def num_to_pattern(index, k):
    if k == 1:
        return digit_to_letter(index)
    prefix = Quotient(index)
    r = Remainder(index, prefix)
    letter = digit_to_letter(r)
    prefixPattern = num_to_pattern(prefix, k - 1)
    return prefixPattern + letter


result = num_to_pattern(dna, k)
print(result.upper())
