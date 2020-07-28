import sys

# with open(sys.argv[1], "r") as file:
#     data = file.readlines()
dna = "GACGATATACGACGATA"
pattern = "ATA"
k = len(pattern)
results = []
for i in range(0, len(dna)-k+1):
    kmer = dna[i:i+k]
    if kmer == pattern:
        print(i)
# seqLen = 9

# with open(sys.argv[2], "w") as results:
#     for i in range(0, len(dna)-seqLen):
#         if dna[i:i+seqLen] in pattern:
#             results.write(str(i) + " ")
