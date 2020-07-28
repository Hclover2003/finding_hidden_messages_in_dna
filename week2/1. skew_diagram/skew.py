text = input("Please input the dna sequence:")
skew = [0]

val = 0
for i in range(len(text)):
    if text[i] == 'C':
        val -= 1
    elif text[i] == 'G':
        val += 1
    skew.append(val)

for i in range(len(skew)):
    print(str(skew[i]), end=" ")
