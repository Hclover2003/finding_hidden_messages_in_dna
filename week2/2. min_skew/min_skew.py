import sys

# with open(sys.argv[1], "r") as file:
#     text = file.read().strip()

text = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
skew = [1]
val = 1
for i in range(len(text)):
    if text[i] == 'C':
        val -= 1
    elif text[i] == 'G':
        val += 1
    skew.append(val)

minval = min(skew)
indices = [i for i, x in enumerate(skew) if x == minval]
print(indices)
