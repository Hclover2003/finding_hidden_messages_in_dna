import sys
# with open(sys.argv[1], 'r') as file:
#     data = file.readlines()
testdna = "ACTGTACGATGATGTGTGTCAAAG"
seqdna = "TGT"
k = len(seqdna)
count = 0
for i in range(0, len(testdna) - k + 1):
    if testdna[i:i+k] in seqdna:
        count += 1
print(count)
