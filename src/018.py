"""

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
37 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

"""

import itertools
import functools
import operator
import time

with open('18.dat') as f:
    rows = [line.strip('\n').split() for line in f.readlines()]
    rows = [[int(i) for i in row] for row in rows]

class Tree(object):
    
    def __init__(self, iterableofiterables):
        self.data = [[i for i in it] for it in iterableofiterables]
        self.routes = [[0]]
        self.current_layer = 0
        self.layers = len(self.data)
        
    def traverse(self, n=None):
        if n is None:
            n = self.layers - 1
        for _ in range(n):
            self.advance()
            self.trim(operator.add)
        
    def advance(self):
        if self.current_layer == self.layers - 1:
            raise ValueError('At the bottom of the tree!')
        self.current_layer += 1
        self.routes =  ([route + [1] for route in self.routes]
                      +[route + [0] for route in self.routes])
        
    def trim(self, func):
        route_dest = {tuple(route): self.locs_from_path(route)[-1][1] for route in self.routes}
        route_dest = sorted(route_dest.items(), key=operator.itemgetter(1))
        
        
        newpaths = []
        for key, group in itertools.groupby(route_dest, operator.itemgetter(1)):
            # key is duplicated but whatever
            maxval, max_idx = 0, 0
            newpath = None
            for idx, (path, key) in enumerate(group):
                val = self.path_value(path, operator.add)
                if val > maxval:
                    maxval = val
                    max_idx = idx
                    newpath = path
            newpaths.append(newpath)
        self.routes = [list(path) for path in newpaths]
                      
    def locs_from_path(self, path):
        current_idx = 0
        current_layer = 0
        locs = [(current_layer, current_idx)]
        for step in path[1:]:
            current_idx += step
            current_layer += 1
            locs.append((current_layer, current_idx))
        return locs
                
    def path_value(self, path, func):
        locs = self.locs_from_path(path)
        vals = [self.data[loc[0]][loc[1]] for loc in locs]
        return functools.reduce(func, vals)
      
    def get_max(self):
        vals = [self.path_value(path, operator.add) for path in 
               self.routes]
        max_path = None
        max_val = 0
        for i, val in enumerate(vals):
            if val > max_val:
                max_val = val
                max_path = self.routes[i]
        return max_val, max_path

#import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline
#nlist =[]
#tlist =[]

#for n in range(2, 100):
#rows = [[np.random.randint(0, 100) for _ in range(i+1)] for i in range(n)]
t = time.time()
T = Tree(rows)
T.traverse()
T.get_max()
#    nlist.append(n)
#    tlist.append(time.time() - t)
    
#plt.plot(nlist, tlist)