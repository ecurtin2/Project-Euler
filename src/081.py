"""

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

$$
\begin{pmatrix}
\color{red}{131} &amp; 673 &amp; 234 &amp; 103 &amp; 18\\
\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; 150\\
630 &amp; 803 &amp; \color{red}{746} &amp; \color{red}{422} &amp; 111\\
537 &amp; 699 &amp; 497 &amp; \color{red}{121} &amp; 956\\
805 &amp; 732 &amp; 524 &amp; \color{red}{37} &amp; \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

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

M = np.loadtxt('081.dat', dtype=int, delimiter=',')
g = arraygraph.ArrayGraph(M)
print(g.minimum_path_val())


