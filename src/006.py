N = 100
sum_squares = sum(i ** 2 for i in range(N + 1))
square_sum = sum(i for i in range(N + 1)) ** 2
print(square_sum - sum_squares)
