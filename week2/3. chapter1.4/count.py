import sys


def count(dna, pattern):
    k = len(pattern)
    count = 0
    for i in range(0, len(testdna) - k + 1):
        if testdna[i:i+k] in seqdna:
            count += 1
    return count
