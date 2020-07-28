# Input: Integers k and t, followed by a collection of strings Dna.
# Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

import sys
import collections
import time
from statistics import mode

# data
with open(sys.argv[1], "r")as file:
    data = file.readlines()
nums = data[0].strip().split(" ")
k = int(nums[0])
t = int(nums[1])
dnastrings = []
for i in range(1, len(data)):
    dnastrings.append(data[i].strip())


def hamming_distance(p, q):
    k = len(p)
    hamd = 0
    for i in range(k):
        if p[i] != q[i]:
            hamd += 1
    return hamd


def profile_list(motiflist):
    profile = []
    k = len(motiflist[0])
    for i in range(k):
        column = []
        columnprof = [1, 1, 1, 1]
        for motif in motiflist:
            column.append(motif[i])
        for letter in column:
            if letter == 'A':
                columnprof[0] += 1
            elif letter == 'C':
                columnprof[1] += 1
            elif letter == 'G':
                columnprof[2] += 1
            elif letter == 'T':
                columnprof[3] += 1
            else:
                print("Error, not a nucleotide")
        for i in range(4):
            columnprof[i] = columnprof[i]/len(motiflist)
        profile.append(columnprof)
    return profile


def prof_prob_kmer(text, k, profile):
    kmerprobs = {}
    for i in range(len(text)-k+1):
        score = 1
        kmer = text[i:i+k]
        for i in range(len(kmer)):
            char = kmer[i]
            if char == 'A':
                x = 0
            elif char == 'C':
                x = 1
            elif char == 'G':
                x = 2
            elif char == 'T':
                x = 3
            else:
                print("Error! not a nucleotide")
            charprob = profile[i][x]
            score = score * charprob
        kmerprobs[kmer] = score
    maxscore = max(kmerprobs.values())
    for key, val in kmerprobs.items():
        if val == maxscore:
            return key


def score(motiflist):
    score = 0
    k = len(motiflist[0])
    for i in range(k):
        col = []
        for motif in motiflist:
            col.append(motif[i])
        sortedcol = sorted(col, key=col.count, reverse=True)
        for char in col:
            if char != sortedcol[0]:
                score += 1
    return score


def greedymotif(dna, k, t):
    bestmotifs = []
    for string in dna:
        bestmotifs.append(string[:k])

    basestrd = dna[0]
    otherstrds = dna[1:]

    # slide through the basestrd
    for i in range(len(basestrd)-k+1):
        kmer = basestrd[i:i+k]
        motiflist = []
        motiflist.append(kmer)

        for i in range(len(otherstrds)):
            currentstring = otherstrds[i]
            profile = profile_list(motiflist)
            prob_kmer = prof_prob_kmer(currentstring, k, profile)
            motiflist.append(prob_kmer)

        print("Motiflist {}: {} | score: {}".format(
            str(i), motiflist, str(score(motiflist))))

        if score(motiflist) < score(bestmotifs):
            bestmotifs = motiflist
    return bestmotifs


print("starting...")
start = time.time()
bestmotifs = greedymotif(dnastrings, k, t)
with open(sys.argv[2], "w")as results:
    for i in range(len(bestmotifs)):
        results.write(bestmotifs[i] + "\n")
end = time.time()
print("done!")
print("That took {} seconds".format(str(end-start)))
