with open("data2.txt", "r")as f:
    data = f.readlines()

with open("res2.txt", "w")as r:
    for e in data:
        r.write(e.strip() + " ")
