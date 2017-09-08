tot = 1
end = 1
N = 1001
for i in range(3, N + 1, 2):
    tot += 10 * (i - 1) + 4 * end
    end = i**2
print(tot)