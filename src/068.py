"""

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

TotalSolution Set
94,2,3; 5,3,1; 6,1,2
94,3,2; 6,2,1; 5,1,3
102,3,5; 4,5,1; 6,1,3
102,5,3; 6,3,1; 4,1,5
111,4,6; 3,6,2; 5,2,4
111,6,4; 5,4,2; 3,2,6
121,5,6; 2,6,4; 3,4,5
121,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?



"""

"""

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

TotalSolution Set
94,2,3; 5,3,1; 6,1,2
94,3,2; 6,2,1; 5,1,3
102,3,5; 4,5,1; 6,1,3
102,5,3; 6,3,1; 4,1,5
111,4,6; 3,6,2; 5,2,4
111,6,4; 5,4,2; 3,2,6
121,5,6; 2,6,4; 3,4,5
121,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?



"""

from collections import defaultdict
import numpy as np
from sympy.utilities.iterables import multiset_permutations


def str_without(string, chars):
    for char in chars:
        string = string.replace(char, '')
    return string


class NGon(object):

    def __init__(self, n):
        assert(n > 2)
        self.N = n
        self.mat = np.eye(self.N, dtype=int) + np.eye(self.N, k=1, dtype=int)
        self.mat[self.N - 1, 0] = 1
        self.mat = np.hstack((self.mat, np.eye(self.N, dtype=int)))
        self.state = np.arange(1, 2*self.N + 1)

        self.min_total = 2 * self.N + 1 + 2
        self.max_total = 3 * (2 * self.N) - 1 - 2

        self.solutions = defaultdict(list)

    def total(self):
        vals = np.dot(self.mat, self.state)
        if np.all(vals == vals[0]):
            return vals[0]
        else:
            return None

    def possible_states(self):
        for state in multiset_permutations(np.arange(1, 2 * self.N + 1)):
            yield state

    def tabulate(self):
        for state in self.possible_states():
            self.state = state
            total = self.total()
            if total:
                if self.state[self.N] == min(self.state[self.N:]):
                    self.solutions[total].append(state)

    def get_string(self, state):
        s = []
        for i in range(self.N):
            s.append(str(state[self.N + i]) + ', ')
            s.append(str(state[i]) + ', ')
            if i < self.N - 1:
                s.append(str(state[i + 1]) + ';  ')
        s.append(state[0])
        return ''.join(str(i) for i in s)

    def table(self):
        for total, states in self.solutions.items():
            for state in states:
                s = self.get_string(state)
                print("Total: {}, state = {}, string = {}".format(total, s, str_without(s, (',', ';', ' '))))


gon = NGon(5)
gon.tabulate()
gon.table()

states = (s for states in gon.solutions.values() for s in states)
strings = (str_without(gon.get_string(s), (',', ';', ' ')) for s in states)
maxstr = max(int(s) for s in strings if len(s) == 16)
print("Max = {}".format(maxstr))

