import itertools
import sys
sys.path.append('./lib')

import sequences

for n in itertools.count():
    if len(str(sequences.fibonacci(n))) == 1000:
        print(n)
        break
