import sys
import time

# with open(sys.argv[1], "r") as file:
#     data = file.readlines()

# k = int(data[0].strip())
# dna_strings = []
# for a in range(1, len(data)):
#     dna_strings.append(data[a].strip())

k = 7
dna_strings = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
               "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC", "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]


def hamming_distance(p, q):
    k = len(p)
    hamd = 0
    for i in range(k):
        if p[i] != q[i]:
            hamd += 1
    return hamd


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


def get_motifs(pattern, dnas):
    k = len(pattern)
    motifs_list = []
    for i in range(len(dnas)):
        dna = dnas[i]
        hd_score = k
        motif = dna[0:k]
        for x in range(len(dna)-k):
            window = dna[x:x+k]
            hamd = hamming_distance(window, pattern)
            if hamd < hd_score:
                motif = window
                hd_score = hamd
        motifs_list.append(motif)

    print(motifs_list)


def get_score(pattern, dnas):
    k = len(pattern)
    tot_hamd = 0
    for i in range(len(dnas)):
        dna = dnas[i]
        hd_score = k
        for x in range(len(dna)-k):
            window = dna[x:x+k]
            hamd = hamming_distance(window, pattern)
            if hamd < hd_score:
                hd_score = hamd
        tot_hamd += hd_score
    return tot_hamd


def get_median(k, dnas):
    distance = float('inf')
    median = []
    scores_list = dict()
    text = "a"*k
    kmers = neighbors(text, k)
    for kmer in kmers:
        score = get_score(kmer, dnas)
        scores_list[kmer] = score

    min_score = min(scores_list.values())
    for kmer in kmers:
        if scores_list[kmer] == min_score:
            median.append(kmer)
    return median


print("Starting...")
start = time.time()
results = get_median(k, dna_strings)
end = time.time()
print(end-start)
print(results)
