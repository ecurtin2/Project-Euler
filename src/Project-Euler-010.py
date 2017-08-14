import itertools as it
import sys
sys.path.append('./lib')
import primes

N = 2e6
val = sum(it.takewhile(lambda x: x < N, primes.eratosthenes()))
print(val)