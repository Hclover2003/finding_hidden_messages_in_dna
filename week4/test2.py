import sys
import time
from _2_gibbs_sample import gibbsSampler

with open(sys.argv[1], "r")as file:
    data = file.readlines()
nums = data[0].split(" ")
k = int(nums[0].strip())
t = int(nums[1].strip())
n = int(nums[2].strip())
dna = []
for i in range(1, len(data)):
    dna.append(data[i].strip())


start = time.time()
print("Starting...")
# with open("res.txt", "w")as res:
#     for i in range(1000):
#         bestmotifs, bestscore = randomized_motif_search(dna, k, t)
#         res.write("{}: {}\n".format(", ".join(bestmotifs), str(bestscore)))

resmotifs = []
resscore = 10000000
for i in range(20):
    x = time.time()
    bestmotifs, bestscore = gibbsSampler(dna, k, t, n, x)
    if i == 0 or bestscore < resscore:
        resmotifs = bestmotifs
        resscore = bestscore

print("{}:{}".format(resmotifs, resscore))

end = time.time()
print("Done! That took {} seconds".format(str(end-start)))
