import functools
import operator
import sys
sys.path.append("./lib")
import fractions


N = 100

nums = []
dens = []
for i in range(10, N):
    for j in range(i):
        num = str(j)
        den = str(i)
        num2, den2 = ''.join([n for n in num if n not in den]), ''.join([n for n in den if n not in num])
        if len(num2) == 1 and len(den2) == 1 and int(den2) != 0 and int(den[1]) != 0:
            v1 = j / i
            v2 = int(num2) / int(den2)
            if abs(v1 - v2) < 1e-9:
                nums.append(j)
                dens.append(i)

print("Fractions are :")
for n, d in zip(nums, dens):
    print("{} / {}".format(n, d))

maxden = functools.reduce(operator.mul, dens)
val = functools.reduce(operator.mul, (x / y for x, y in zip(nums, dens)))
frac = fractions.Fraction.from_float(val).limit_denominator(maxden)
print("The reduced fraction is: {}".format(frac))
print("Making the denominator: {} ".format(frac.denominator))