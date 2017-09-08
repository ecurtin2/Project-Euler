import sys
sys.path.append("./lib")

def pentagonal_nums(n):
    return (n * (3 * n - 1)) // 2

p = pentagonal_nums
nums = set(pentagonal_nums(i) for i in range(1, 10**5))
l1 = [(p(k), p(j)) for k in range(1, 10**4) for j in range(1, k)
      if p(k) + p(j) in nums and p(k) - p(j) in nums]
print(l1[0][1] - l1[0][0])

