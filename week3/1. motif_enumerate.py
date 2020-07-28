# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1], "r") as file:
    data = file.readlines()
    nums = data[0].split(" ")
    k = int(nums[0])
    d = int(nums[1])

    text = data[1:]
    text = [i.strip() for i in text]


def hamming_distance(p, q):
    k = len(p)
    hamd = 0
    for i in range(k):
        if p[i] != q[i]:
            hamd += 1
    return hamd


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


# MotifEnumeration(Dna, k, d)
#         Patterns ← an empty set
#         for each k-mer Pattern in Dna
#             for each k-mer Pattern’ differing from Pattern by at most d mismatches
#                 if Pattern' appears in each string from Dna with at most d mismatches
#                     add Pattern' to Patterns
#         remove duplicates from Patterns
#         return Patterns


def motif_enumerate(dna_list, k, d):
    kmer_set = [set() for _ in range(len(dna_list))]
    for x in range(len(dna_list)):
        dna = dna_list[x]
        for i in range(len(dna)-k+1):
            kmer = dna[i:i+k]
            kmer_neighbors = neighbors(kmer, d)
            for neighbor in kmer_neighbors:
                if neighbor not in kmer_set[x]:
                    kmer_set[x].add(neighbor)
    return kmer_set


result = motif_enumerate(text, k, d)


u = set.intersection(*result)

with open(sys.argv[2], "w") as txtfile:
    for mystring in u:
        txtfile.write(mystring + " ")
