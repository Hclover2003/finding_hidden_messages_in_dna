import sys
import time
from _1_randomized_motif_search import randomized_motif_search

# with open(sys.argv[1], "r")as file:
#     data = file.readlines()
# nums = data[0].split(" ")
# k = int(nums[0].strip())
# t = int(nums[1].strip())
# dna = []
# for i in range(1, len(data)):
#     dna.append(data[i].strip())


# start = time.time()
# print("Starting...")
# # with open("res.txt", "w")as res:
# #     for i in range(1000):
# #         bestmotifs, bestscore = randomized_motif_search(dna, k, t)
# #         res.write("{}: {}\n".format(", ".join(bestmotifs), str(bestscore)))

# resdict = {}
# setlist = []


mdna = ['AAGCCAAA', 'AATCCTGG', 'GCTACTTG', 'ATGTTTTG']
# for i in range(1):
bestmotifs, bestscore = randomized_motif_search(mdna, 3, 4, time.time())
print(bestmotifs)
# setmotifs = set(bestmotifs)
# strmotifs = ", ".join(bestmotifs)
# if (i == 0) or (setmotifs not in setlist):
#     setlist.append(setmotifs)
#     resdict[strmotifs] = bestscore

# results = {k: v for k, v in sorted(
#     resdict.items(), key=lambda item: item[1])}

# reslist = []
# for key, val in results.items():
#     if val == min(results.values()):
#         reslist.append(key)

# print(reslist)
end = time.time()
print("Done! That took {} seconds".format(str(end-start)))
