import re
import operator
import functools
import time

t = time.time()

with open("8.dat") as f:
    s = re.sub('[\s+]', '', f.read())

N = 13

chunks = [i for i in s.split('0') if len(i) >= N]

for i in range(1, 10):
    temp = []
    for chunk in chunks:
        for subchunk in chunk.split(str(i)):
            if len(subchunk) >= N:
               temp.append(subchunk)
             
    if len(temp) == 0:
        break
    chunks = temp 

max_val = 0
print(chunks)
for chunk in chunks:
    ints = [int(v) for v in list(chunk)] 
    val = functools.reduce(operator.mul, ints)
    if val > max_val:
        max_val = val

print(max_val) 
print("completed in {:4.4} microseconds.".format((time.time() - t) * 1e6))
