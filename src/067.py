import itertools
import functools
import operator
import time

with open('67.dat') as f:
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