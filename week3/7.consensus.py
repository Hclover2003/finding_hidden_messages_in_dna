profile = [[0.4, 0.3, 0.0, 0.1, 0.0, 0.9]

           [0.2, 0.3, 0.0, 0.4, 0.0, 0.1]

           [0.1, 0.3, 1.0, 0.1, 0.5, 0.0]

           [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]]


def consensus(profile):
    k = len(profile[0])
    consensus = []
    for i in range(k):
        col = []
        for x in range(4):
            col.append(profile[x][i])
        maxnum = max(col)
        for num in col:
            if num == maxnum:

    result = ''.join(consensus)
    return result
