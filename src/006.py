"""

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

N = 100
sum_squares = sum(i ** 2 for i in range(N + 1))
square_sum = sum(i for i in range(N + 1)) ** 2
print(square_sum - sum_squares)
