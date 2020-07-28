from utils import profile_list, motifs_list, score
import random


def randomized_motif_search(dna, k, t, x):
    random.seed(x)
    motifs = ['CCA', 'CCT', 'CTT', 'TTG']
    # for dnastr in dna:
    #     randnum = random.randint(0, len(dnastr)-k)
    #     motifs.append(dnastr[randnum:randnum+k])
    bestmotifs = motifs
    while True:
        profile = profile_list(motifs)
        motifs = motifs_list(profile, dna, k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs, score(bestmotifs)
