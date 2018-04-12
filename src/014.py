"""

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

"""

from collections import OrderedDict

class LimitedSizeDict(OrderedDict):
    def __init__(self, size_limit=128, *args, **kwds):
        self.size_limit = size_limit
        OrderedDict.__init__(self, *args, **kwds)
        self._check_size_limit()

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.size_limit is not None:
            while len(self) > self.size_limit:
                self.popitem(last=False)

class collatz_count():
    
    def __init__(self):
        self.count = 0
        self.found = {}
        
    def collatz_recursion(self, val):
        
        # lookup cache if the value has been found
        # this will always hit after first val=1
        if val in self.found.keys():
            self.count += self.found[val]
        else:        
            self.count += 1
            if val > 1:
                if val % 2 == 0:
                    val = val // 2
                    self.collatz_recursion(val)
                else:
                    val = 3 * val + 1
                    self.collatz_recursion(val)
                
    def __call__(self, val):
        self.count = 0 
        self.collatz_recursion(val)
        self.found[val] = self.count
        return self.count
    
    
    
cc = collatz_count()

N = 10**6
max_starter, max_count = 0, 0

for i in range(N):
    count = cc(i)
    if count > max_count:
        max_starter = i
        max_count = count
        
print(max_starter, max_count)