from math import floor, sqrt


def contfrac_from_decimal(S):
    m = [0]
    d = [1]
    a = [int(floor(S))]
    while a[-1] != (2 * a[0]):
        m.append(d[-1] * a[-1] - m[-1])
        d.append((round(S**2) - m[-1]**2) / d[-1])
        a.append(floor((S + m[-1]) / d[-1]))
    return a[0], a[1:]

N = 10001
nums = (sqrt(i) for i in range(N) if not sqrt(i).is_integer())
periods = [len(contfrac_from_decimal(n)[1]) for n in nums]
print(sum(1 for p in periods if p % 2 != 0))

