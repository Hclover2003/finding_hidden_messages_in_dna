from __future__ import print_function
from count import count
import sys
import time

# with open(sys.argv[1], "r") as file:
#     data = file.readlines()

# text = data[0].strip()
# nums = data[1].split(" ")
# k = int(nums[0].strip())
# d = int(nums[1].strip())


def hamming_distance(p, q):
    k = len(p)
    hamd = 0
    for i in range(k):
        if p[i] != q[i]:
            hamd += 1
    return hamd


def approx_substring_indices(pattern, text, d):
    results = []
    count = 0
    for i in range(len(text)-len(pattern)+1):
        tmp = text[i:i+len(pattern)]
        distance = hamming_distance(tmp, pattern)
        if distance <= d:
            results.append(i)
            count += 1
    return results, count


def reverse_complement(pattern):
    rc_pattern = ""
    for i in range(len(pattern)):
        if pattern[i] == 'A':
            rc_pattern += 'T'
        elif pattern[i] == 'T':
            rc_pattern += 'A'
        elif pattern[i] == 'G':
            rc_pattern += 'C'
        elif pattern[i] == 'C':
            rc_pattern += 'G'
    my_pattern = rc_pattern[::-1]
    return my_pattern


def neighbors(pattern, d):
    # if exact match, return pattern
    if d == 0:
        return [pattern]
    # if length 1, neighbors are each of the 4 nucleotides
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighbourhood = []
    suffix = pattern[1:]
    # strings that differ from pattern[i:] by d or less mismatches
    suffix_neighbours = neighbors(suffix, d)
    # for each string in the neighbours of the given pattern - 1
    for text in suffix_neighbours:
        # if differs from string by at most 1 less than d
        if hamming_distance(suffix, text) < d:
            # adds a prefix to the pattern, adds to the pattern neighbourhood
            for i in ['A', 'C', 'G', 'T']:
                neighbourhood.append(i+text)
        # if differs from string by d, just add it to the neighbourhood with exact match for first letter
        else:
            neighbourhood.append(pattern[0]+text)
    return neighbourhood


pattern = "ACGT"
result = neighbors(pattern, 3)
print(len(result))


def freqkmer(text, k, d):
    freqdict = {}
    for i in range(len(text)-k+1):
        window = text[i:i+k]
        rc_pattern = reverse_complement(window)
        rc_pattern_neighbors = neighbors(rc_pattern, d)
        window_neighbors = neighbors(window, d)
        for a in rc_pattern_neighbors:
            if a in freqdict.keys():
                freqdict[a] += 1
            else:
                freqdict[a] = 1
        for e in window_neighbors:
            if e in freqdict.keys():
                freqdict[e] += 1
            else:
                freqdict[e] = 1
    return freqdict


# print("starting...")
# start = time.time()
# results = freqkmer(text, k, d)
# maxval = max(results.values())
# myres = []
# for key, val in results.items():
#     if val == maxval:
#         myres.append(key)

# end = time.time()
# print("Done" + str(start-end))
# for i in range(len(myres)):
#     print(myres[i], end=' ')


# results = neighbors(pattern, d)

# with open(sys.argv[2], "w") as myres:
#     for i in range(len(results)):
#         myres.write(results[i]+'\n')
