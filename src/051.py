import itertools as it


import sympy

digits = [str(i) for i in range(10)]
primes = list(sympy.ntheory.primerange(10**4, 10**5))
blacklist = set()
current_max = (0, 0)

for p in primes:
    if p not in blacklist:
        s = str(p)
        for n in range(1, len(s) - 1):
            for i in it.combinations(range(len(s) - 1), n):
                vals = []
                for d in digits:
                    news = []
                    for idx in range(len(s)):
                        if idx in i:
                            news.append(d)
                        else:
                            news.append(s[idx])
                    vals.append(int(''.join(news)))
                myset = set(v for v in vals if v in primes)
                count = len(myset)
                if count < current_max[0]:
                    for thing in myset:
                        blacklist.add(thing)
                else:
                    current_max = count, myset
                if current_max == 7:
                    break

print(current_max[0], sorted(current_max[1]))