with open("13.dat") as f:
    val = sum((int(line) for line in f.readlines()))
print(str(val)[:10])