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