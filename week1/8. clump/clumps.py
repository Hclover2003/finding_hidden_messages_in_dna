import sys

import sys


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
    for i in range(0, 4**k):
        freq_array.append(0)
    for i in range(0, len(text) - k+1):
        pattern = text[i:i+k]
        index = pattern_to_num(pattern)
        freq_array[index] += 1
    return freq_array


with open(sys.argv[1], "r") as file:
    data = file.readlines()
text = data[0].strip()
nums = data[1].strip().split(" ")
k = int(nums[0])
L = int(nums[1])
t = int(nums[2])


def freq_dict_maker(window, k, L, t, tmp_dict, results):
    # add to dictionary that maps
    # each kmer -> # of times it occurs within window
    for a in range(len(window)-k + 1):
        kmer = window[a:a+k]
        if kmer in tmp_dict:
            tmp_dict[kmer] += 1
        else:
            tmp_dict[kmer] = 1
    for key, value in tmp_dict.items():
        if value >= t:
            results.append(key)
    return tmp_dict, results


def clump_finder(genome, k, L, t):
    results = []
    # slides window of length L down genome
    for i in range(0, len(genome) - L + 1):
        window = genome[i:i+L]
        if i == 0:
            tmp_dict = {}
            results = []
        else:
            tmp_dict, results = freq_dict_maker(
                genome[i-1:i-1+L], k, L, t, tmp_dict, results)
        for key, value in tmp_dict.items():
            if value >= t:
                results.append(key)
    return results


myresults = clump_finder(text, k, L, t)
print(myresults)
