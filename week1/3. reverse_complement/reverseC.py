import sys

with open(sys.argv[1], "r") as file:
    data = file.read()
    rcString = []
    separator = ""
    print(len(data))

for i in range(0, len(data)):
    if data[i] == 'T':
        rcString.append('A')
    elif data[i] == 'A':
        rcString.append('T')
    elif data[i] == 'C':
        rcString.append('G')
    elif data[i] == 'G':
        rcString.append('C')

newString = separator.join(rcString)[::-1]
with open("results.txt", "w") as results:
    results.write(newString)
