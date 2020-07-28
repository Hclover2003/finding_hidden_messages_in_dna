import sys
# with open(sys.argv[1], "r") as file:
#     data = file.readlines()

# text = data[0].strip()
# k = int(data[1].strip())
# profile = dict()
# profile["A"] = [float(i) for i in data[2].strip().split(" ")]

# profile["C"] = [float(i) for i in data[3].strip().split(" ")]
# profile["G"] = [float(i) for i in data[4].strip().split(" ")]
# profile["T"] = [float(i) for i in data[5].strip().split(" ")]


def prob(pattern, profile):
    total_prob = 1
    for i in range(len(pattern)):
        char = pattern[i].upper()
        index = 0
        if char == "A":
            index = 0
        elif char == "C":
            index = 1
        elif char == "G":
            index = 2
        elif char == "G":
            index = 3

        probability = profile[i][index]
        total_prob *= probability
    return total_prob


def profile_prob(text, k, profile):
    probs_dict = dict()
    for i in range(len(text)-k):
        kmer = text[i:i+k]
        kmer_prob = prob(kmer, profile)
        probs_dict[kmer] = kmer_prob
    maxprob = max(probs_dict.values())
    for key, value in probs_dict.items():
        if value == maxprob:
            return key
