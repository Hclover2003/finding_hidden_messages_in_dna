import random


def prof_prob(kmer, profile):
    # loop through kmer each character
    kmerprob = 1
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
        kmerprob = kmerprob * charprob
    return kmerprob


def prof_prob_kmer(text, k, profile):
    kmerprobs = {}
    for i in range(len(text)-k+1):
        score = 1
        kmer = text[i:i+k]
        kmerprobs[kmer] = prof_prob(kmer, profile)
    maxscore = max(kmerprobs.values())
    for key, val in kmerprobs.items():
        if val == maxscore:
            return key


def prof_random_kmer(text, k, profile):
    kmerprobs = {}
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        kmerprob = prof_prob(kmer, profile)
        kmerprobs[kmer] = kmerprob
    profrandkmer = random.choices(
        population=list(kmerprobs.keys()), weights=list(kmerprobs.values()), k=1)
    return profrandkmer


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


#note: motiflist
def profile_list(motiflist):
    # returns [[0,1,0,0],[0.2,1,0.1,0.3],.....k]
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
                print("Error, not a nucleotide", letter)
        for i in range(4):
            columnprof[i] = columnprof[i]/len(motiflist)
        profile.append(columnprof)
    return profile


def motifs_list(profilelist, dna, k):
    motifslist = []
    for dnastr in dna:
        prob_kmer = prof_prob_kmer(dnastr, k, profilelist)
        motifslist.append(prob_kmer)
    return motifslist
