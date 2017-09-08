import numpy as np
import itertools
import functools
import collections
import time


def count_consecutive_occurances(iterable, condition):
    applied = [condition(i) for i in iterable]
    counts = [ sum(1 for _ in group) for key, group 
             in itertools.groupby(applied) if key ]
    return counts

def has_n_consecutive(iterable, condition, n):
    counts = count_consecutive_occurances(iterable, condition)
    return any((count >= n for count in counts))

def has_any(ary, N):
    iterables = [row for row in ary]
    iterables += [col for col in ary.T]
    ndiags = ary.shape[0] - N
    diags = [np.diag(ary, i) for i in range(-ndiags, ndiags)]
    reverse_diags = [np.diag(np.fliplr(grid), i) 
                      for i in range(-ndiags, ndiags)]
    iterables += diags

    return any(has_n_consecutive(it, lambda x: x >= 0, n=N) 
        for it in iterables)   

def gen_from_row(row, N):
    where = np.where(row < 0)[0]
    temps = [i[i > 0] for i in np.split(row, where) if len(i) >= N]

    gen = []
    for temp in temps:
        for i in range(len(temp) - N + 1):
            gen.append(temp[i: i+N])       
    return gen
        
def locate(ary, N):
    found = collections.defaultdict(list)
    rows = (row for row in ary)
    cols = (col for col in ary.T)
    ndiags = grid.shape[0] - N
    diags = [np.diag(ary, i) for i in range(-ndiags, ndiags)]
    reverse_diags = [np.diag(np.fliplr(grid), i) 
                      for i in range(-ndiags, ndiags)]
    
    for i, row in enumerate(rows):
        if has_n_consecutive(row, lambda x: x >= 0, n=N):
            found['row'].append(gen_from_row(row, N))
            
    for i, row in enumerate(cols): 
        if has_n_consecutive(row, lambda x: x >= 0, n=N):
            found['col'].append(gen_from_row(row, N))
            
    for i, row in enumerate(diags):
        if has_n_consecutive(row, lambda x: x >= 0, n=N):
            found['diag'].append(gen_from_row(row, N))

    for i, row in enumerate(reverse_diags):
        if has_n_consecutive(row, lambda x: x >= 0, n=N):
            found['rdiag'].append(gen_from_row(row, N))
    return found


N = 4
#M = 150
grid = np.loadtxt("11.dat", dtype=int)
#grid = np.random.randint(0, high=100, size=(M, M))

t = time.time()
temp = np.copy(grid)
for i in itertools.count():
    mean = np.mean(temp[temp != -1])
    lessthan = temp < mean
    temp[lessthan] = -1
    if has_any(temp, N):
        grid = np.copy(temp)
    else:
        break


found = locate(grid, N)

vals = []
for ary_list in found.values():
    for ary in ary_list:
        vals.append(np.prod(ary))

val = max(vals)
print(val)
print("Found in {} seconds.".format(time.time() - t))