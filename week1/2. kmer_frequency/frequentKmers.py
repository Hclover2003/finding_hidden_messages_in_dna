import sys
# compute most frequent k-mer

# with open(sys.argv[1], "r") as file:
#     data = file.readlines()
text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k = 3
mydict = {}

for i in range(0, len(text) - k + 1):
    kmer = text[i:i+k]
    if kmer in mydict.keys():
        mydict[kmer] += 1
    else:
        mydict[kmer] = 1

sorteddict = {k: v for k, v in sorted(
    mydict.items(), reverse=True, key=lambda item: item[1])}

print(sorteddict)
# maxNum = list(mydict.values())[0]

# with open(sys.argv[2], "w") as results:
#     for key, value in mydict.items():
#         if value == maxNum:
#             results.write(key + "\n")
