import random
import sys
import random
from utils import profile_list, prof_random_kmer, score


def gibbsSampler(dna, k, t, N, x):
    # initialize bestmotifs as motifs
    random.seed(x)
    motifs = []
    for dnastr in dna:
        randnum = random.randint(0, len(dnastr)-k)
        motifs.append(dnastr[randnum:randnum+k])
    bestmotifs = motifs

    # for N iterations
    for i in range(1, N):
        i = random.randint(0, t-1)
        motifs.pop(i)
        # profile_list
        profile = profile_list(motifs)
        motifi = prof_random_kmer(dna[i], k, profile)[0]
        motifs.insert(i, motifi)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs, score(bestmotifs)
