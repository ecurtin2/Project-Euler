"""

NOTE: This problem is a more challenging version of Problem 81.
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

$$
\begin{pmatrix}
131 &amp; 673 &amp; \color{red}{234} &amp; \color{red}{103} &amp; \color{red}{18}\\
\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; 150\\
630 &amp; 803 &amp; 746 &amp; 422 &amp; 111\\
537 &amp; 699 &amp; 497 &amp; 121 &amp; 956\\
805 &amp; 732 &amp; 524 &amp; 37 &amp; 331
\end{pmatrix}
$$

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

"""

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

zeros = np.zeros_like(M)
ary = np.hstack((zeros, M, zeros))

g = arraygraph.ArrayGraph(ary, up=True)
print(g.minimum_path_val())