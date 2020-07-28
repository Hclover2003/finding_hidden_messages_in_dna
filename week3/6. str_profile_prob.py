profile = [[0.4, 0.3, 0.0, 0.1, 0.0, 0.9],

           [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],

           [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],

           [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]]

mystr = "GAGCTA"


def str_profile_prob(dna, profile):
    prob = 1
    for i in range(len(dna)):
        char = dna[i]
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
        prob = prob*profile[x][i]
    return prob


result = str_profile_prob(mystr, profile)
print(result)
