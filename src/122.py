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