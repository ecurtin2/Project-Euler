import functools
import operator

s = ''.join(str(i) for i in range(10**6))
vals = [int(s[10 ** i]) for i in range(7)]
print(vals)
print(functools.reduce(operator.mul, vals))