"""

Consider quadratic Diophantine equations of the form:
x2 – Dy2 = 1
For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
32 – 2×22 = 1
22 – 3×12 = 192 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

"""

"""

Consider quadratic Diophantine equations of the form:
x2 – Dy2 = 1
For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
32 – 2×22 = 1
22 – 3×12 = 192 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

"""


from math import sqrt, floor
import collections
import itertools as it

N = 1000
squares = [i**2 for i in range(N)]
non_squares = [i for i in range(N) if i not in squares]


def convergents(a0, an_list):
    h = collections.deque([0, 1], maxlen=2)
    k = collections.deque([1, 0], maxlen=2)
    a = it.chain([a0], it.cycle(an_list))
    while True:
        a_n = next(a)
        h_next = a_n * h[1] + h[0]
        k_next = a_n * k[1] + k[0]
        h.append(h_next)
        k.append(k_next)
        yield h_next, k_next


def contfrac_from_decimal(S):
    m = [0]
    d = [1]
    a = [int(floor(S))]
    while a[-1] != (2 * a[0]):
        m.append(d[-1] * a[-1] - m[-1])
        d.append((round(S**2) - m[-1]**2) / d[-1])
        a.append(floor((S + m[-1]) / d[-1]))
    return a[0], a[1:]

N = 1001
d_list = [i for i in range(1, N) if not sqrt(i).is_integer()]
Solution = collections.namedtuple('Solution', ['x', 'y', 'd'])
sols = []
for d in d_list:
    a0, rest = contfrac_from_decimal(sqrt(d))
    for h, k in convergents(a0, rest):
        if (h**2 - d * k**2) == 1:
            sols.append(Solution(x=h, y=k, d=d))
            break

print(max(sols, key=lambda s: s.x))

