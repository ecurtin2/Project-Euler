import sys
sys.path.append('../customlib')
import numpy as np
import arraygraph


test = np.asarray([ [131, 673, 234, 103,  18]
                   ,[201,  96, 342, 965, 150]
                   ,[630, 803, 746, 422, 111]
                   ,[537, 699, 497, 121, 956]
                   ,[805, 732, 524,  37, 331]
                ], dtype=int)

M = np.loadtxt('083.dat', dtype=int, delimiter=',')
g = arraygraph.ArrayGraph(test, up=True)

vals = []
nrows = test.shape[0]
for istart in range(nrows):
    for iend in range(nrows):
        vals.append(g.minimum_path_val(start=(istart, 0), destination=(iend, nrows - 1)))

print(min(vals))