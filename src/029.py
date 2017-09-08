import itertools
combs = itertools.product(range(2, 101), repeat=2)
print(len(set((a**b for a, b in combs))))