import math

quizlist = [[0.5, 0, 0, 0.5],

            [0.25, 0.25, 0.25, 0.25],

            [0, 0, 0, 1],

            [0.25, 0, 0.5, 0.25]]


def entropy(profile_col):
    summed = 0
    for elem in profile_col:
        if elem == 0:
            ent = 0
        else:
            ent = elem*(math.log(elem, 2))
        summed += ent
    summed = -summed
    return summed


for mylist in quizlist:
    print(entropy(mylist))
