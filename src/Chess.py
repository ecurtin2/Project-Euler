from copy import copy
from math import sqrt

import numpy as np
import itertools as it


class Node(object):
    num_instances = 0

    def __init__(self, loc, val):
        __class__.num_instances += 1
        self.loc = loc
        self.val = val
        self.label = __class__.num_instances
        self.connected = set()
        self.probabilities = {}
        self.probability_cache = {}

    def set_initial(self, probability=0.0):
        self.probabilities[self.val] = probability

    def connect(self, other):
        self.connected.add(other)

    def update(self):
        self.probabilities = copy(self.probability_cache)
        self.probability_cache = {}

    def take(self, prob):
        for k, v in prob.items():
            new_k = k + self.val
            if new_k in self.probability_cache.keys():
                self.probability_cache[new_k] += v
            else:
                self.probability_cache[new_k] = v

    def step(self):
        n = len(self.connected)
        split = {k: v / n for k, v in self.probabilities.items()}  # Here it's assumed equal probability per connected
        if len(split) > 0:
            for node in self.connected:
                node.take(split)

    def __str__(self):
        return 'Nodes[{}, {}] = {}  Current vals: {}'.format(self.loc[0], self.loc[1], self.val, self.probabilities)


class Board(object):
    moves = {
        'upleft': np.array((-1, 2))
        , 'upright': np.array((1, 2))
        , 'rightup': np.array((2, 1))
        , 'rightdown': np.array((2, -1))
        , 'downright': np.array((1, -2))
        , 'downleft': np.array((-1, -2))
        , 'leftdown': np.array((-2, -1))
        , 'leftup': np.array((-2, 1))
    }

    def __init__(self, N):
        board = np.arange(N**2, dtype=int).reshape((N, N))
        self.N = N
        self.indices = np.concatenate(np.indices(board.shape).T)
        self.nodes = [[None]*N for _ in range(N)]

        for val, idx in zip(board.flatten(), self.indices):
            self.nodes[idx[0]][idx[1]] = Node(idx, val)

        for node in self.all_nodes():
            for move in __class__.moves.values():
                new_pos = node.loc + move
                if np.all(new_pos < N) and np.all(new_pos >= 0):
                    node.connect(self.nodes[new_pos[0]][new_pos[1]])

    def __getitem__(self, loc):
        """Return reference to the node at i, j location."""
        i, j = loc
        return self.nodes[i][j]

    def set_initial(self, loc_vals=None):
        if loc_vals is None:
            loc_vals = {(0, 0): 1.0}
        else:
            if abs(sum(loc_vals.values()) - 1.0) > 1e-8:
                raise ValueError('Sum of initial probabilities must equal 1.0')

        for loc, val in loc_vals.items():
            self[loc[0], loc[1]].set_initial(val)

    def all_nodes(self):
        return sorted(it.chain.from_iterable(self.nodes), key=lambda n: n.val)

    def step(self):
        for node in self.all_nodes():
            node.step()
        # must be done after all steps, values for next step are cached
        for node in self.all_nodes():
            node.update()

    def vals(self):
        totals = {}
        for n in self.all_nodes():
            for val, prob in n.probabilities.items():
                if val in totals.keys():
                    totals[val] += prob
                else:
                    totals[val] = prob
        return totals

    def moment(self, order):
        return sum(prob * val**order for val, prob in self.vals().items())

    def __str__(self):
        return '\n'.join(str(node) for node in self.all_nodes())

np.set_printoptions(linewidth=200)
b = Board(4)
b.set_initial({(1, 1): 0.5, (3, 2): 0.5})

nsteps = 40
prev = 0.0
for n in range(nsteps):
    b.step()
    vals = b.vals()
    mean = b.moment(1)
    var = b.moment(2) - mean ** 2
    print("Step {:3}:{:8.2f} +/-{:15.10f}  {}".format(n+1, mean, sqrt(var), mean - prev))
    prev = mean
