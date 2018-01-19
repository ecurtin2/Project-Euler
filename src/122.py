"""

The most naive way of computing n15 requires fourteen multiplications:
n × n × ... × n = n15
But using a "binary" method you can compute it in six multiplications:
n × n = n2n2 × n2 = n4n4 × n4 = n8n8 × n4 = n12n12 × n2 = n14n14 × n = n15
However it is yet possible to compute it in only five multiplications:
n × n = n2n2 × n = n3n3 × n3 = n6n6 × n6 = n12n12 × n3 = n15
We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 ≤ k ≤ 200, find ∑ m(k).

"""

import math
import functools
import pprint



class PowOptimizer(object):

    def __call__(self, n):
        self.visits = {}
        return self._opt_pows(n)


    #@functools.lru_cache(maxsize=200)
    def _opt_pows(self, n, visits=tuple()):
        visits += (n,)
        if n == 1:
            return 0, visits
        if n == 2:
            return 1, visits

        vals_visits = []
        imax = int(math.ceil(n // 2)) + 1
        for i in range(1, imax):
            j = n - i
            if i == j:
                val, visits = self._opt_pows(i, visits)
                val += 1
                vals_visits.append((val, visits))
            else:
                cost_i, visits_i = self._opt_pows(i, visits)
                cost_j, visits_j = self._opt_pows(j, visits)
                visits = tuple(set(visits_i).union(set(visits_j)))
                val = 1 + cost_i + cost_j
                vals_visits.append((val, visits))

        return min(vals_visits, key=lambda x: x[0])


P = PowOptimizer()
d = {n: P._opt_pows(n) for n in range(1, 16)}

pprint.pprint(d)