import math

with open('099.dat') as f:
    pairs = f.read().splitlines()

maxval = 0
for i, pair in enumerate(pairs):
    base, exp = (int(i) for i in pair.split(','))
    val = exp * math.log(base)
    if val > maxval:
        maxval = val
        maxrow = i + 1

print(maxrow)