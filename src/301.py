import numpy as np
import time

def X(n):
    n = int(n)
    return bool(n ^ (2 * n) ^ (3 * n))


N = 2**28

t = time.time()
n = np.arange(1, N)
x = np.bitwise_xor(n, np.bitwise_xor(2*n, 3*n)).astype(bool)
total = np.sum(x)
print("Numpy done in {:10.8f} seconds.".format(time.time() - t))
print(total)

#t = time.time()
#total = sum(X(i) for i in range(1, N))
#print("Python done in {:10.8f} seconds.".format(time.time() - t))
#print(total)