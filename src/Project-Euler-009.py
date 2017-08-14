N = 1000
for b in range(N):
    for a in range(b):
        c = N - a - b
        if (a < b < c) and (a**2 + b**2 == c**2):
            print("Triplet = {}, {}, {}, product = {}".format(
                a, b, c, a * b * c))